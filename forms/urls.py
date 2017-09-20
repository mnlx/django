from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name='forms'

urlpatterns = [

    url(r'^create/$', views.survey_create,name='surveycreate'),
    url(r'^json/$', views.form_list ,name='survey_list'),
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^survey/$', views.SurveyList.as_view()),
    url(r'^survey/(?P<pk>[0-9]+)/$', views.SurveyDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]



urlpatterns = format_suffix_patterns(urlpatterns)

# print(urlpatterns)