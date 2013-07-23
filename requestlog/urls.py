from django.conf.urls import patterns, url

from requestlog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index')
        )
