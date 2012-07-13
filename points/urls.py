from django.conf.urls import url, patterns

urlpatterns = patterns('points.views',
    url(r'^$', 'index'),
    url(r'^getAllPoints', 'getAllPoints'),
    url(r'^create/$', 'create'),
    #url(r'^savePointToDB$', 'savePointToDB'), old for ajax method
)