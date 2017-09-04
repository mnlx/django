from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from rango.models import User,Friends
from django.core.urlresolvers import reverse
from .forms import MessagesForm
from django.contrib.auth.decorators import login_required
from django.db.models import F,Q
from conversations.models import Messages
from django.http import JsonResponse
# from .filters import filters
import datetime
# Create your views here.
@login_required
def conversations(request):

    # conv = Conversations.objects.get(pk=1)
    friends  = request.user.friends_set.all()
    friends_name_list =[]
    for friend in friends:

        if friend.friend_id != 0:
            friends_name_list.append( User.objects.get(pk=int(friend.friend_id)).username )
            print(User.objects.get(pk=int(friend.friend_id)).username)
    return render(request, 'conversations/friends.html', {'friends':friends_name_list})

@login_required
def friends(request):
    list_friends = request.user.friends_set.all()[:5]
    list_friends_id = []
    for i in list_friends:
        list_friends_id.append(i.friend_id)

    list_friends = User.objects.filter(id__in =list_friends_id )

    list_friends_excluded = User.objects.all().exclude(id__in=list_friends)[:5]

    if request.method == 'POST':
        return HttpResponse(request.POST['id'])
    return render(request, 'conversations/friends.html', {'not_friends':list_friends_excluded})

def messages(request):
    frd_lst = [i.friend_id for i in request.user.friends_set.all()]
    friends = User.objects.filter(pk__in=frd_lst)

    form = MessagesForm()
    frd_id = request.user.friends_set.all()[0].friend_id
    if request.method == 'POST':

        form = MessagesForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            a = form.save()

            a.add(data['text'],request.user,User.objects.get(pk=frd_id),sender=1)
            a.save()

            return HttpResponseRedirect(reverse('conversations:messages'))

    msg = Messages.objects.filter( Q(mtm = User.objects.get(id = frd_id))).filter( Q( mtm = request.user) )

    form['text'].label = 'Message'
    return render(request, 'conversations/messages.html', {'form':form , 'friends':friends[:6], 'msg':msg})

def  json(request):
    return JsonResponse({'foo':'bar'})

def jsontester(request):
    return render(request, 'conversations/jsontester.html',{})