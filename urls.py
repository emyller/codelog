# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

from django.conf import settings

## static files
if not settings.IN_PRODUCTION:
    urlpatterns += patterns('',
        (r'^{0}/(?P<path>.*)$'.format(settings.MEDIA_URL[1:-1]), 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        })
    )
