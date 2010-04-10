# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'datetime', 'tags_',
    list_filter = 'datetime',
    date_hierarchy = 'datetime'
    search_fields = 'title', 'text',

admin.site.register(models.Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = 'name', 'posts_',

admin.site.register(models.Tag, TagAdmin)
