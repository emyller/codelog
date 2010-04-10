# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'datetime',

admin.site.register(models.Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = 'name',

admin.site.register(models.Tag, TagAdmin)
