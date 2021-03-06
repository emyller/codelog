# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    text = models.TextField()
    datetime = models.DateTimeField()
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    views = models.IntegerField(default=0)
    draft = models.BooleanField()

    def __unicode__(self):
        return '{title} ({date})'.format(
            date = self.datetime,
            title = self.title
        )

    def get_absolute_url(self):
        return '/post/' + self.slug

    class Meta:
        ordering = '-datetime',

    ## properties
    @property
    def html_text(self):
        from django.contrib.markup.templatetags.markup import markdown
        return markdown(self.text, 'safe,codehilite')

    ## display methods
    def tags_(self):
        return ', '.join([tag[0] for tag in self.tags.values_list('name')])

class Tag(models.Model):
    name = models.SlugField(max_length=40)

    def __unicode__(self):
        return self.name

    ## display methods
    def posts_(self):
        return self.posts.count()
