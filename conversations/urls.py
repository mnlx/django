from conversations import views
from django.conf.urls import url

app_name = 'conversations'

urlpatterns = [
    url(r'^$', views.conversations, name='index'),
    url(r'^friends/$', views.friends, name='friends'),
    url(r'^add_friends/$', views.add_friends, name='add_friends'),
    url(r'^remove_friends/$', views.remove_friends, name='remove_friends'),

]