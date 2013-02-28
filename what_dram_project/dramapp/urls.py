from django.conf.urls import patterns, url

from dramapp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^whisky/$', views.whisky, name='whisky'),
        url(r'^distillery/$', views.distillery, name='distillery'),
)