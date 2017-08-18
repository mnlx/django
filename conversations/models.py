from django.db import models
from rango.models import User,Friends
from datetime import datetime
# Create your models here.

class Messages(models.Model):
    mtm = models.ManyToManyField(User)
    text = models.CharField(max_length=1000)
    pub_date = models.DateField(null=True)
    sender_id = models.IntegerField(null=True)


    def add(self,text, *args, **kwargs):
        # Force to add only two people per message
        print('Added both to base')

        self.mtm.add(args[0],args[1])
        self.text = text

    def save(self, *args, **kwargs):
        self.pub_date = datetime.now()
        super(Messages, self).save()

    class Meta:
        order_with_respect_to = 'pub_date'


class MessageStats(models.Model):

    size = models.CharField(max_length=1,choices=(('S','Small'),('B','Big')))





