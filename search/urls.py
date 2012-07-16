from django.conf.urls import url, patterns
from search.views import search

urlpatterns = patterns('search.views',
    url(r'^(.*)', search),
)