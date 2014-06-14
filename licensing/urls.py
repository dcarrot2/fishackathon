from django.conf.urls import patterns, url

from licensing import views

urlpatterns = patterns('',
       url(r'^$', views.licensing, name='index'),
)
    

