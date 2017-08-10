from django.db import models
from rango.models import User
# Create your models here.

class Conversations(models.Model):

    message = models.CharField(max_length=144)
    date = models.DateField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('message',)