from django.conf.urls import patterns, url

from registration import views

urlpatterns = patterns('',
       url(r'^A/$', views.registrationA, name='registrationA'),
       url(r'^B/$', views.registrationB, name='registrationB')
       
)