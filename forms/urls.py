from django.conf.urls import url
from . import views

app_name='forms'

urlpatterns = [

    url(r'^create/$', views.survey_create,name='surveycreate'),
    url(r'^json/$', views.form_list ,name='survey_list'),
]