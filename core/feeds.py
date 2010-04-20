# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from models import Post

class RSSFeed(Feed):
    title = 'EvandroMyller.blog'
    link = 'http://blog.emyller.net/latest/'
    description = 'Latest posts from EvandroMyller.blog'
    items = lambda self: Post.objects.all()

    item_title       = lambda s, post: post.title
    item_description = lambda s, post: post.html_text
    item_author_name = lambda s, post: post.author.first_name or post.author.username
    item_pubdate     = lambda s, post: post.datetime
