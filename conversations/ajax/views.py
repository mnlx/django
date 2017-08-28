from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from rango.models import User,Friends
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def add_friends(request):


    if request.method == 'GET':
        friend_id = request.GET['friend_id']

        user = request.user
        user_id = request.user.id
        user = User.objects.get(pk= int(user_id))

        if friend_id == user_id:
            return HttpResponse('Forget about it')
        user.friends_set.get_or_create(friend_id = friend_id).save()

    return HttpResponse('teehee')

def remove_friends(request):


    if request.method == 'GET':
        friend_id = request.GET['friend_id']
        print(friend_id)
        user_id = request.user.id
        print(user_id)
        # user = User.objects.get(pk= int(user_id))
        request.user.friends_set.filter(friend_id = friend_id)[0].delete()

    return HttpResponse('teehee')

