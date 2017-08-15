from django import forms
from django.contrib.auth.models import User
from .models import Conversations

class ConversationsForm(forms.ModelForm):
    message = forms.CharField(help_text='Write your message')
    date = forms.DateField()

    class Meta:
        model = Conversations
        fields = ('date',)