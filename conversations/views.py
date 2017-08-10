from django.shortcuts import render
from conversations.models import Conversations
# Create your views here.
def conversations(request):
    conv = Conversations.objects.get(pk=1)
    return render(request, 'conversations/conversations.html',{'msg1':conv})