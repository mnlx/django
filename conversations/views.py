from django.shortcuts import render,HttpResponse
from rango.models import User
from conversations.models import Conversations
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
    list_users = User.objects.all()[:15]
    if request.method == 'POST':
        return HttpResponse(request.POST['id'])
    return render(request, 'conversations/friends.html', {'users':list_users})

def add_friends(request):

    # cat_id = None
    if request.method == 'GET':
        friend_id = request.GET['friend_id']
        user_id = request.GET['user_id']


        user = User.objects.get(pk= int(user_id))
        user.friends_set.create(friend = friend_id).save()
        # if cat_id:
        #     cat = Category.objects.get(id=int(cat_id))
        #     if cat:
        #         cat.likes += 1
        #         cat.save()
        #         likes = cat.likes
    return HttpResponse('teehee')