# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Page.order'
        db.add_column(u'site_page', 'order',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Page.order_uk'
        db.add_column(u'site_page', 'order_uk',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.order_ru'
        db.add_column(u'site_page', 'order_ru',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.order_en'
        db.add_column(u'site_page', 'order_en',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Page.order'
        db.delete_column(u'site_page', 'order')

        # Deleting field 'Page.order_uk'
        db.delete_column(u'site_page', 'order_uk')

        # Deleting field 'Page.order_ru'
        db.delete_column(u'site_page', 'order_ru')

        # Deleting field 'Page.order_en'
        db.delete_column(u'site_page', 'order_en')


    models = {
        u'site.client': {
            'Meta': {'object_name': 'Client'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'site.clientquote': {
            'Meta': {'object_name': 'ClientQuote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_en': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_ru': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_uk': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'site.page': {
            'Meta': {'ordering': "('order', 'title')", 'object_name': 'Page'},
            'category': ('django.db.models.fields.IntegerField', [], {'default': '2', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_en': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_ru': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_uk': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'order_en': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'order_ru': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'order_uk': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'short_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_text_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_text_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'site.topslider': {
            'Meta': {'object_name': 'TopSlider'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'uk'", 'max_length': '8'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['site']