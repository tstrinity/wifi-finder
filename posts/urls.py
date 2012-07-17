__author__ = 'ts.trinity'

from django.conf.urls import url, patterns

urlpatterns = patterns('posts.views',
    url(r'^$', 'index'),
    url(r'(?P<post_id>\d+)/$', 'details'),
)