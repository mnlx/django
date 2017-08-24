from django import forms
from django.contrib.auth.models import User
from .models import Messages
import datetime
class MessagesForm(forms.ModelForm):

    text = forms.CharField(help_text='Message',max_length=1000,widget=forms.Textarea(), required=True)


    class Meta:
        model = Messages
        fields = ('text',)

