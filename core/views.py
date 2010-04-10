# -*- coding: utf-8 -*-
from django.views.generic import list_detail
from django.db.models import Q
from models import *

def latest(req):
    posts = Post.objects.all()
    rpp = int(req.GET.get('rpp') or 5)
    page = int(req.GET.get('page') or 1)

    if req.GET.get('tag'):
        posts = posts.filter(tags__name=req.GET['tag'])
    if req.GET.get('q'):
        posts = posts.filter(Q(title__icontains=req.GET['q']) | Q(text__icontains=req.GET['q']))

    print posts
    return list_detail.object_list(req,
        queryset = posts,
        paginate_by = rpp,
        template_name = 'core/latest.html',
        template_object_name = 'post',
        extra_context = {
            'rpp': rpp,
            'min_display_page': 1 if page - 5 < 0 else page - 5
        },
    )

def view_post(req, post_id):
    return list_detail.object_detail(req,
        queryset = Post.objects.all(),
        object_id = post_id,
        template_name = 'core/post.html',
        template_object_name = 'post',
        extra_context = { 'show_comments': True },
    )
