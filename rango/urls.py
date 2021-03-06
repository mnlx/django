from rango import views
from django.conf.urls import url


app_name = 'rango'




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<pk>[0-9]+)/(?P<pq>[0-9]+)$', views.number, name='number'),
    url(regex=r'^category/(?P<category_name_slug>[\w\-]+)/$', view=views.category, name='category'),
    url(regex=r'^add_category/$', view=views.add_category, name='add_category'),
    url(regex=r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', view=views.add_page, name='add_page'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^like/$', views.like_category, name='like_category'),
    url(r'^suggest/$', views.suggest_category, name='sugest_category'),



]
