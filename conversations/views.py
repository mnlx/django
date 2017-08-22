from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from rango.models import User
from django.core.urlresolvers import reverse
from .forms import MessagesForm
from django.contrib.auth.decorators import login_required
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
    list_friends = request.user.friends_set.all()
    list_friends_id = []
    for i in list_friends:
        list_friends_id.append(i.friend_id)

    list_friends = User.objects.filter(id__in =list_friends_id )

    list_friends_excluded = User.objects.all().exclude(id__in=list_friends)[:15]

    if request.method == 'POST':
        return HttpResponse(request.POST['id'])
    return render(request, 'conversations/friends.html', {'not_friends':list_friends_excluded,
                                                          'friends': list_friends})
@login_required
def add_friends(request):

    # cat_id = None
    if request.method == 'GET':
        friend_id = request.GET['friend_id']
        user_id = request.GET['user_id']
        user = User.objects.get(pk= int(user_id))

        if friend_id == user_id:
            return HttpResponse('Forget about it')
        user.friends_set.get_or_create(friend_id = friend_id).save()

    return HttpResponse('teehee')

def remove_friends(request):

    # cat_id = None
    if request.method == 'GET':
        friend_id = request.GET['friend_id']
        user_id = request.GET['user_id']
        user = User.objects.get(pk= int(user_id))

        user.friends_set.get_or_create(friend = friend_id)[0].delete()

    return HttpResponse('teehee')

def messages(request):
    form = MessagesForm()
    if request.method == 'POST':
        print('psoted')
        form = MessagesForm(request.POST)
        # form.mtm.add(request.user)

        print(form)

        a = form.save()
        a.add('sds',User.objects.get(pk=1),User.objects.get(pk=2),sender=1)
        a.save()
        print(form.errors)
        return HttpResponseRedirect(reverse('conversations:messages'))

    return render(request, 'conversations/messages.html', {'form':form})