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