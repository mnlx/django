from django.db import models
from rango.models import User,Friends
from datetime import datetime
# Create your models here.

class Conversations(models.Model):


    message = models.CharField(max_length=144)

    users = models.ForeignKey(Friends, default=None)
    date = models.DateField(default=None)