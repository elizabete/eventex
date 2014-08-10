from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('eventex.core.views',
    url(r'^$', 'homepage', name='homepage'),
)

from django.conf import settings
urlpatterns += patterns('django.views.static',
    url(r'^static/(?P<path>.*)$', 'serve',
        {'document_root': settings.STATIC_ROOT}),
)
