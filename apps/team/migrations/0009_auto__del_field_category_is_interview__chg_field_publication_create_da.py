# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Category.is_interview'
        db.delete_column(u'team_category', 'is_interview')


        # Changing field 'Publication.create_date'
        db.alter_column(u'team_publication', 'create_date', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):
        # Adding field 'Category.is_interview'
        db.add_column(u'team_category', 'is_interview',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Publication.create_date'
        db.alter_column(u'team_publication', 'create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        u'team.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'team.member': {
            'Meta': {'object_name': 'Member'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'team.publication': {
            'Meta': {'object_name': 'Publication'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Member']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Category']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 8, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'short_text': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['team']