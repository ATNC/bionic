from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^(?P<cur_user>\S+)/$', 'twitter.views.twitfilter'),




)
