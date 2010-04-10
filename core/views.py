# -*- coding: utf-8 -*-
from django.views.generic import list_detail
from models import *

def home(req):
    return list_detail.object_list(req,
        queryset = Post.objects.all(),
        paginate_by = int(req.GET.get('rpp') or 5),
        template_name = 'core/home.html',
        template_object_name = 'post',
    )
