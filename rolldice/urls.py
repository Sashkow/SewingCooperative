from django.conf.urls import patterns, url
from rolldice import views

urlpatterns = patterns('',
    url(r'^initial/$', views.rolldice, name='roll-dice'),
    url(r'^ajax/$', views.rolldice_ajax, name='roll-dice-ajax'),

)