# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Publication.category'
        db.alter_column(u'news_publication', 'category', self.gf('django.db.models.fields.IntegerField')(max_length=1))

        # Changing field 'Publication.top_banner'
        db.alter_column(u'news_publication', 'top_banner', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Publication.category'
        db.alter_column(u'news_publication', 'category', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Publication.top_banner'
        db.alter_column(u'news_publication', 'top_banner', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

    models = {
        u'news.publication': {
            'Meta': {'object_name': 'Publication'},
            'category': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_top': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'short_text': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'top_banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['news']