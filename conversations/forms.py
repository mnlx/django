from django import forms
from django.contrib.auth.models import User
from .models import Messages

class MessagesForm(forms.ModelForm):
    # def __init__(self,usr1,usr2, *args, **kwargs):
    #
    #     if kwargs.get('instance'):
    #         initial= kwargs.setdefault('initial',{})
    #         initial['mtm'] = [i.pk for i in kwargs['instance'].messages_set]
    #
    #     forms.ModelForm.__init__(self, *args, **kwargs)

    text = forms.CharField(help_text='Write your message',max_length=1000,widget=forms.Textarea(), required=True)
    pub_date = forms.DateField(widget=forms.SelectDateWidget())
    mtm = forms.ModelChoiceField(queryset=User.objects.filter(pk__in=[1,2]))

    # mtm = forms.ModelForm()
    class Meta:
        model = Messages
        fields = ('pub_date','text')

