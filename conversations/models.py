from django.db import models
from rango.models import User,Friends
from datetime import datetime
# Create your models here.

class Messages(models.Model):
    mtm = models.ManyToManyField(User)
    text = models.CharField(max_length=100)

    def add_2(self,text, *args, **kwargs):
        # Force to add only two people per message
        print(args)
        self.mtm.add(args[0])
        self.mtm.add(args[1])
        self.text = text
        super(Messages, self).save(*args, **kwargs)

class Conversations(models.Model):


    message = models.CharField(max_length=144)
    users = models.ForeignKey(Friends, default=None)
    date = models.DateField(default=None)

class MessageStats(models.Model):

    size = models.CharField(max_length=1,choices=(('S','Small'),('B','Big')))


class Person(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name

class Group(models.Model):
    name  = models.CharField(max_length=123)
    members = models.ManyToManyField(Person, through='Membership',related_name='%(class)s_%(class)s')

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    date_joined = models.DateField( )
