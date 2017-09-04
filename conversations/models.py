from django.db import models
from rango.models import User,Friends
import datetime

# Create your models here.

class Searchy(models.Manager):
    def countin(self):
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT m.text
            FROM conversations_messages m
            WHERE m.id > 40
            GROUP BY m.id
            ORDER BY m.pub_date            
            """)

            return(cursor.fetchall())


class Messages(models.Model):
    mtm = models.ManyToManyField(User)

    text = models.CharField(max_length=1000)
    pub_date = models.DateField(null=True)
    sender_id = models.IntegerField(null=True)

    # objects = Searchy()

    def add(self,text, *args, **kwargs):
        # Force to add only two people per message
        print('Added both to base')

        self.mtm.add(args[0],args[1])
        self.text = text
        if kwargs['sender']:
            self.sender_id = kwargs['sender']

    def save(self, *args, **kwargs):
        self.pub_date = datetime.date.today()
        super(Messages, self).save()

    class Meta:
        order_with_respect_to = 'pub_date'




class MessageStats(models.Model):

    size = models.CharField(max_length=1,choices=(('S','Small'),('B','Big')))





