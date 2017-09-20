from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import viewsets,renderers


app_name = 'analise'

analise_html = views.AnaliseViewSet.as_view({
    'get': 'analise_html'
}, renderer_classes=[renderers.StaticHTMLRenderer])



urlpatterns = [


    url(r'^list/$', views.AnaliseViewSet.as_view({'get':'list'}), name='analise-list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.AnaliseViewSet.as_view({'get':'retrieve'}), name='analise-detail'),
    url(r'^detail/(?P<pk>[0-9]+)/html$', analise_html, name='html-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

# print(urlpatterns)