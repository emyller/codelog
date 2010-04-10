# -*- coding: utf-8 -*-
from django.views.generic import list_detail
from models import *

def latest(req):
    posts = Post.objects.all()
    if req.GET.get('tag'): posts = posts.filter(tags__name=req.GET['tag'])
    return list_detail.object_list(req,
        queryset = posts,
        paginate_by = int(req.GET.get('rpp') or 5),
        template_name = 'core/latest.html',
        template_object_name = 'post',
    )

def view_post(req, post_id):
    return list_detail.object_detail(req,
        queryset = Post.objects.all(),
        object_id = post_id,
        template_name = 'core/post.html',
        template_object_name = 'post',
        extra_context = { 'show_comments': True }
    )
