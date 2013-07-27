# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.is_interview'
        db.add_column(u'team_category', 'is_interview',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Publication.short_text'
        db.add_column(u'team_publication', 'short_text',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.is_interview'
        db.delete_column(u'team_category', 'is_interview')

        # Deleting field 'Publication.short_text'
        db.delete_column(u'team_publication', 'short_text')


    models = {
        u'team.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_interview': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'team.member': {
            'Meta': {'object_name': 'Member'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'team.publication': {
            'Meta': {'object_name': 'Publication'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Member']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Category']"}),
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'short_text': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['team']