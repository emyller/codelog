# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
import views

urlpatterns = patterns('core.views',
    url(r'^$', 'home'),
)
