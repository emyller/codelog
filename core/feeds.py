# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from models import Post

class LatestPostsFeed(Feed):
    title = 'EvandroMyller.blog latest posts'
    link = '/latest/'
    description = 'Latest entries from EvandroMyller.blog'

    def items(self): return Post.objects.all()
    def item_title(self, post): return post.title
    def item_link(self, post): return post.get_absolute_url()
    def item_description(self, post): return post.html_text
