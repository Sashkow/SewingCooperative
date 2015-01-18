from django.conf.urls import patterns, url
from rolldice import views

urlpatterns = patterns('',
    url(r'^$', views.rolldice, name='roll-dice'),
)