from django.conf.urls import url, patterns
from polls.ajax import poll_ajax_vote, poll_ajax_result

urlpatterns = patterns('',
    url(r'^vote/(?P<poll_pk>\d)$', poll_ajax_vote, name='poll_ajax_vote'),
    url(r'^result/(?P<poll_pk>\d)$', poll_ajax_result, name='poll_ajax_result'),
)
