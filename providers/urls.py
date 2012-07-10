__author__ = 'ts.trinity'

from django.conf.urls import url, patterns

urlpatterns = patterns('providers.views',
    url(r'^$', 'index'),
    url(r'^getAllProviders', 'getAllProviders'),
)