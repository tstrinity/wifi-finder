from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from mocca import settings

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    url(r'^posts/', include('posts.urls')),
    url(r'^points/', include('points.urls')),
    url(r'^providers/', include('providers.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^poll/', include('polls.urls')),
    #url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^about/', 'direct_to_template', {'template' : 'about.html'}),
    (r'^$', 'direct_to_template', {'template': 'index.html'}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)