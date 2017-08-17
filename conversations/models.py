from django.db import models
from rango.models import User,Friends
from datetime import datetime
# Create your models here.

class Messages(models.Model):
    mtm = models.ManyToManyField(User)
<<<<<<< HEAD
    text = models.CharField(max_length=1000)
    pub_date = models.DateField()
    sender_id = models.IntegerField(null=True)

    def add(self,text, *args, **kwargs):
        # Force to add only two people per message
        self.mtm.add(args[0])
        self.mtm.add(args[1])
        self.text = text
        self.sender_id = args[0].id
=======
    text = models.CharField(max_length=100)
    pub_date = models.DateField()


    def add(self,text, *args, **kwargs):
        # Force to add only two people per message
        print('Added both to base')

        self.mtm.add(args[0],args[1])
        self.text = text

    def save(self, *args, **kwargs):
        self.pub_date = datetime.now()
        super(Messages, self).save()



class Conversations(models.Model):


    message = models.CharField(max_length=144)
    users = models.ForeignKey(Friends, default=None)
    date = models.DateField(default=None)

class MessageStats(models.Model):

    size = models.CharField(max_length=1,choices=(('S','Small'),('B','Big')))


class Person(models.Model):
    name = models.CharField(max_length=123)

>>>>>>> 194f9d6d6438f47137d918ec809a4a173b5cb045
    def __str__(self):
        return str(self.mtm.all())

    class Meta:
        order_with_respect_to = 'pub_date'


