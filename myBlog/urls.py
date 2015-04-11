from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # http://DomainName/blog/ ---> go to blog.urls
    url(r'^blog/', include('blog.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns(
                'blog.views.static',
                (r'^media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}),
                )