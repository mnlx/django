from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from rango.models import User,Friends
from django.db.models import Q,F
from conversations.models import Messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def add_friends(request):
    if request.method == 'GET':
        friend_id = request.GET['friend_id']
        request.user.friends_set.get_or_create(friend_id = friend_id)

    return HttpResponse('This is supposed to be a get')


def remove_friends(request):
    if request.method == 'GET':
        friend_id = request.GET['friend_id']
        request.user.friends_set.filter(friend_id = friend_id)[0].delete()

    return HttpResponse('This is supposed to be a get')

def get_messages(request):

    friend_id = request.GET['friend_id']
    print(User.objects.get(pk=friend_id))
    msg = Messages.objects.filter(mtm=request.user).filter(mtm=User.objects.get(pk=friend_id))[:5]

    msg_send = {}
    print(msg)
    for i,m in enumerate(msg):
        print(m)
        msg_send[i] = m.text

    print(msg_send)
    return JsonResponse(msg_send)