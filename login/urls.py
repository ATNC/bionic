from django.conf.urls import patterns,  url


urlpatterns = patterns('',

        # Examples:
        # url(r'^$', 'firstapp.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),


    url(r'^login/', 'login.views.login'),
    url(r'^logout/', 'login.views.logout'),
    url(r'^register/', 'login.views.register'),














)
