# -*- coding: utf-8 -*-
# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Post.slug'
        db.add_column('core_post', 'slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=100, db_index=True), keep_default=False)

        print 'Updating slug fields...'
        from ..models import Post
        from django.template.defaultfilters import slugify
        posts = Post.objects.all()
        if posts.count():
            i, l = .0, posts.count()
            for post in posts:
                post.slug = slugify(post.title)
                post.save()
                i += 1
                print '{0:3}% #{1} - {2}'.format(i / l * 100, post.id, post)
            print 'Done.'
        else:
            print 'No posts yet.'


    def backwards(self, orm):
        
        # Deleting field 'Post.slug'
        db.delete_column('core_post', 'slug')


    models = {
        'core.post': {
            'Meta': {'object_name': 'Post'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'posts'", 'blank': 'True', 'to': "orm['core.Tag']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['core']
