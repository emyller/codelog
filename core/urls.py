# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
import views, feeds

urlpatterns = patterns('core.views',
    url(r'^$', redirect_to, { 'url': 'latest/'}),
    url(r'^latest/$', 'latest', name='home'),
    url(r'^tag/([\w-]+)$', 'tag_view', name='tag_view'),
    #url(r'^post/(\d+)$', 'view_post', name='post'),
    url(r'^post/([\w-]+)$', 'view_post', name='post'),

    ## feeds
    url(r'^rss$', feeds.LatestPostsFeed(), name='rss')
)
