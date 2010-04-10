# -*- coding: utf-8 -*-
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime = models.DateTimeField()
    tags = models.ManyToManyField('Tag', blank=True)

    def __unicode__(self):
        return '{title} ({date})'.format(
            date = self.datetime,
            title = self.title
        )

class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name
