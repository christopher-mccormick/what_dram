from django.conf.urls import patterns, url

from dramapp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index')
)