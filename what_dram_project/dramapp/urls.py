from django.conf.urls import patterns, url
from dramapp.models import Region, Distillery, Whisky
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from dramapp import views

whisky_info = {
    'queryset': Whisky.objects.all(),
    'template_name': 'dramapp/whisky.html',
    'template_object_name': 'whisky',
    #need to append age
}

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        #url(r'^whisky/$', views.whisky, name='whisky'),
        url(r'^whisky/$', list_detail.object_list, whisky_info),
        url(r'^distillery/$', views.distillery, name='distillery'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
      
)