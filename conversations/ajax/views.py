from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from rango.models import User,Friends
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

