from django.db import models
from rango.models import User,Friends
from datetime import datetime
# Create your models here.

class Messages(models.Model):
    mtm = models.ManyToManyField(User)
    text = models.CharField(max_length=1000)
    pub_date = models.DateField()
    sender_id = models.IntegerField(null=True)

    def add(self,text, *args, **kwargs):
        # Force to add only two people per message
        self.mtm.add(args[0])
        self.mtm.add(args[1])
        self.text = text
        self.sender_id = args[0].id
    def __str__(self):
        return str(self.mtm.all())

    class Meta:
        order_with_respect_to = 'pub_date'


