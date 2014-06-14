from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fishackathon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('registration.urls', namespace='index')),
    url(r'^registration/', include('registration.urls', namespace='registration')),
    url(r'^licensing/', include('licensing.urls', namespace='licensing')),
    url(r'^reporting', include('reporting.urls', namespace='reporting')),
)
