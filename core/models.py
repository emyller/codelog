# -*- coding: utf-8 -*-
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime = models.DateTimeField()
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __unicode__(self):
        return '{title} ({date})'.format(
            date = self.datetime,
            title = self.title
        )

    def get_absolute_url(self):
        return '/post/' + str(self.pk)

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
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

    ## display methods
    def posts_(self):
        return self.posts.count()
