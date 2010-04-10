# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
import views

urlpatterns = patterns('core.views',
    url(r'^$', redirect_to, { 'url': 'latest/'}, name='home'),
    url(r'^latest/$', 'latest'),
    url(r'^post/(?P<post_id>\d+)$', 'view_post', name='post'),
)
