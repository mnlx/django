from conversations import views
from django.conf.urls import url
from django.conf.urls import include
app_name = 'conversations'

urlpatterns = [
    url(r'^$', views.conversations, name='index'),
    url(r'^friends/$', views.friends, name='friends'),
    url(r'^ajax/', include('conversations.ajax.urls')),
    # url(r'^remove_friends/$', views.remove_friends, name='remove_friends'),
    url(r'^messages/', views.messages, name='messages')

]
