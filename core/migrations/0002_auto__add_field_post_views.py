# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Post.views'
        db.add_column('core_post', 'views', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Post.views'
        db.delete_column('core_post', 'views')


    models = {
        'core.post': {
            'Meta': {'object_name': 'Post'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
