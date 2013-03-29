
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'porta.views.home', name='home'),
    #url(r'^porta/', include('porta.portapp.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

#    (r'^accounts/login/$', 'django.contrib.auth.views.login'),

    (r'^porta/portapp/', include('portapp.urls')),

)
