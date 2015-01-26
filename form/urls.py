from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'twitter.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('login.urls')),
    url(r'^page/(\d+)/$', 'twitter.views.index'),
    url(r'^cmnts/', include('twitter.urls')),


)
