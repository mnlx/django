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
    url(r'^register/$', views.register, name='registration'),
    url(r'^login/$', views.user_login, name='login'),
    # url(r'^logout/$', views.signout, name='logout'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted')


]
