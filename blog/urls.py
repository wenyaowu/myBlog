__author__ = 'evanwu'
from django.views.generic.simple import direct_to_template
from django.conf.urls import patterns, url
from blog import views
import feed
# create url pattern, must named urlpatterns
urlpatterns = patterns('',
                       # url(url pattern, view, name)
                       # http://DomainName/blog/(urlpattern) ---> Go to view
                       url(r'^$', views.index, name='index'),
                       url(r'^about_me/', views.about_me, name='about_me'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
                       url(r'^article/(?P<article_title_slug>[\w\-]+)/$', views.article, name='article'),
                       url(r'^feed/$', feed.LatestPosts(), name='feed'),
                       url(r'^tag/(?P<tag_name_slug>[\w\-]+)/$', views.tag, name='tag'),
                       url(r'^googlefee7078ca97b9445.html/$', views.google, name='google'),
                       url(r'^technoratimedia_sv_14ee3.txt$', direct_to_template,
     						{'template': 'technoratimedia_sv_14ee3.txt', 'mimetype': 'text/plain'})
                       )
