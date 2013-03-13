from django.conf.urls import patterns, url
from django.conf.urls import *
from dramapp import views
from dramapp.views import rate

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^distillery/$', views.distillery, name='distillery'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^search/$', views.search, name='search'),
                       url(r'^whisky/(?P<whisky_name_url>\w+)', views.whisky, name='whisky'),
                       url(r'^distillery/(?P<distillery_name_url>\w+)', views.distilleries_list,
                           name='distilleries_list'),
                       url(r'^comments/', include('django.contrib.comments.urls')),
                       url(r'^whisky/(?P<whisky_name_url>\w+)$', rate, name='dramapp_whisky_rate'),
                       url(r'^ratings/', include('ratings.urls')),
)