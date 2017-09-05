from django.conf.urls import url
from . import views

app_name='forms'

urlpatterns = [

    url(r'^create/$', views.survey_create,name='surveycreate'),
]