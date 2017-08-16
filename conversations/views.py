from django.shortcuts import render,HttpResponse
from rango.models import User
from conversations.models import Conversations
from .forms import ConversationsForm
# Create your views here.
def conversations(request):

    # conv = Conversations.objects.get(pk=1)
    friends  = request.user.friends_set.all()
    friends_name_list =[]
    for friend in friends:

        if friend.friend != 0:
            friends_name_list.append( User.objects.get(pk=int(friend.friend)).username )
            print(User.objects.get(pk=int(friend.friend)).username)
    return render(request, 'conversations/conversations_base.html', {'friends':friends_name_list})

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
    form = ConversationsForm
    if request.method == 'POST':
        form = ConversationsForm(request.POST)

    return render(request, 'conversations/messages.html', {'form':form})