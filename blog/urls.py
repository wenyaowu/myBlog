__author__ = 'evanwu'

from django.conf.urls import patterns, url
from blog import views

# create url pattern, must named urlpatterns
urlpatterns = patterns('',
                       # url(url pattern, view, name)
                       # http://DomainName/blog/(urlpattern) ---> Go to view
                       url(r'^$', views.index, name='index'),
                       url(r'^about_me/', views.about_me, name='about_me'),)