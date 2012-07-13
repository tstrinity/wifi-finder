__author__ = 'ts.trinity'

from django.conf.urls import url, patterns
from django.views.decorators.cache import cache_page

urlpatterns = patterns('posts.views',
    url(r'^$', 'index'),
    url(r'(?P<post_id>\d+)/$', 'details'),
)