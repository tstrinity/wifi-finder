__author__ = 'ts.trinity'

from django.conf.urls import url, patterns

urlpatterns = patterns('points.views',
    url(r'^$', 'index'),
    url(r'^getAllPoints', 'getAllPoints'),
#    url(r'^add$', 'add'), old for ajax, use create method
    url(r'^create/$', 'create'),
#    url(r'^savePointToDB$', 'savePointToDB'), old for ajax method
)