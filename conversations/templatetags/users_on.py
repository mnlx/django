from django import template
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from rango.models import User
register = template.Library()
import datetime

@register.inclusion_tag('conversations/templatetags/users_on.html')
def users_on():

    # conv = Conversations.objects.get(pk=1)
    friends  = User.objects.all()[:5]
    friends_name_list =[(x.first_name,x.last_name) for x in friends]

    return {'online_friends' : friends_name_list}

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)