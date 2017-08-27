from . import views
from django.conf.urls import url

app_name = 'ajax'

urlpatterns = [
    url(r'^add_friends/$', views.add_friends, name='add_friends'),

]
