# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^', include(settings.PROJECT_ALIAS + '.core.urls', namespace='core')),
)

## static files
if not settings.IN_PRODUCTION:
    urlpatterns += patterns('',
        (r'^{0}/(?P<path>.*)$'.format(settings.MEDIA_URL[1:-1]), 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        })
    )
