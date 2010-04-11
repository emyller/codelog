# -*- coding: utf-8 -*-
from django.views.generic import list_detail
from django.views.decorators.cache import cache_page
from django.db.models import Q
from models import *

@cache_page(20 * 60)
def latest(req, tag_name=''):
    posts = Post.objects.filter(draft=False).select_related()
    rpp = int(req.GET.get('rpp') or 5)
    page = int(req.GET.get('page') or 1)

    if tag_name:
        posts = posts.filter(tags__name=tag_name)
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

def tag_view(req, tag_name):
    return latest(req, tag_name)

def view_post(req, slug):
    post = Post.objects.filter(draft=False).get(slug=slug)
    if not req.user.is_authenticated():
        post.views += 1
        post.save()
    return list_detail.object_detail(req,
        queryset = Post.objects.all().select_related(),
        object_id = post.pk,
        template_name = 'core/post.html',
        template_object_name = 'post',
        extra_context = { 'show_comments': True },
    )
