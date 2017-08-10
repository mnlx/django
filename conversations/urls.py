from conversations import views
from django.conf.urls import url

app_name = 'conversations'

urlpatterns = [
    url(r'^$', views.conversations, name='index'),

]