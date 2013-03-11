from django.conf.urls import patterns, url
from dramapp.models import Region, Distillery, Whisky, Rating
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from dramapp import views
from dramapp.views import rate

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^distillery/$', views.distillery, name='distillery'),
        #url(r'^(\w+)/$', whisky),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^search/$', views.search, name='search'),
	url(r'^whisky/(?P<whisky_name_url>\w+)', views.whisky, name='whisky'),
	url(r'^distillery/(?P<distillery_name_url>\w+)', views.distilleries_list, name='distilleries_list'),
	url(r'^comments/', include('django.contrib.comments.urls')),
        url(r'^(?P<whisky_id>\d+)$', rate, name='rate'),
        #url(r'^distillery/(?P<distillery_name_url>\w+)', views.distillery_archive, name='distillery_archive')
        #url(r'^comment/$', views.comments, name='comments'),
        #url(r"^comment/$", views.add_comment, name="add_comment"),
        #url(r'^thanks/$', views.thanks, name='thanks')     
)