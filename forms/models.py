from django.db import models
from rango.models import User
import datetime
# Create your models here.

class Survey(models.Model):

    def __init__(self,*args,**kargs):

        super(Survey, self).__init__(*args,**kargs)
        self.date_created = datetime.datetime.now()


    date_created = models.DateTimeField(null=True)
    user = models.ForeignKey(User)

class TextField(models.Model):

    extends = models.ForeignKey(Survey)

    identifier = models.CharField(max_length=10,null=False)

    name = models.CharField(max_length=30,null=True)


class TextFieldAnswers(models.Model):

    extends = models.ForeignKey(TextField)
    user = models.IntegerField()

    text = models.TextField(max_length=1000,null=True)


class DateField(models.Model):

    extends = models.ForeignKey(Survey)

    identifier = models.CharField(max_length=10,null=False)

    name = models.CharField(max_length=30,null=True)



class DateFieldAnswers(models.Model):
    extends = models.ForeignKey(DateField)
    user = models.IntegerField()

    date = models.DateTimeField(null=True)



class CheckField(models.Model):

    extends = models.ForeignKey(Survey)

    identifier = models.CharField(max_length=10,null=False)

    name = models.CharField(max_length=30,null=True)



class CheckFieldAnswers(models.Model):
    extends = models.ForeignKey(CheckField)
    user = models.IntegerField()

    check = models.NullBooleanField(null=True)


class ChoiceField(models.Model):

    extends = models.ForeignKey(Survey)

    identifier = models.CharField(max_length=10,null=False)

    name = models.CharField(max_length=30,null=True)

class ChoiceFieldOptions(models.Model):

    extends = models.ForeignKey(ChoiceField)

    name = models.CharField(max_length=30,null=True)



class ChoiceFieldAnswers(models.Model):
    extends = models.ForeignKey(ChoiceFieldOptions)
    user = models.IntegerField()

    choice = models.NullBooleanField(null=True)



