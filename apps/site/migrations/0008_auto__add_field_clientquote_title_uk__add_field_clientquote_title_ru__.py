# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ClientQuote.title_uk'
        db.add_column(u'site_clientquote', 'title_uk',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ClientQuote.title_ru'
        db.add_column(u'site_clientquote', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ClientQuote.title_en'
        db.add_column(u'site_clientquote', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ClientQuote.text_uk'
        db.add_column(u'site_clientquote', 'text_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ClientQuote.text_ru'
        db.add_column(u'site_clientquote', 'text_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ClientQuote.text_en'
        db.add_column(u'site_clientquote', 'text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ClientQuote.is_active_uk'
        db.add_column(u'site_clientquote', 'is_active_uk',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ClientQuote.is_active_ru'
        db.add_column(u'site_clientquote', 'is_active_ru',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ClientQuote.is_active_en'
        db.add_column(u'site_clientquote', 'is_active_en',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Page.title_uk'
        db.add_column(u'site_page', 'title_uk',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.title_ru'
        db.add_column(u'site_page', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.title_en'
        db.add_column(u'site_page', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.text_uk'
        db.add_column(u'site_page', 'text_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.text_ru'
        db.add_column(u'site_page', 'text_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.text_en'
        db.add_column(u'site_page', 'text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.short_text_uk'
        db.add_column(u'site_page', 'short_text_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.short_text_ru'
        db.add_column(u'site_page', 'short_text_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.short_text_en'
        db.add_column(u'site_page', 'short_text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Page.is_active_uk'
        db.add_column(u'site_page', 'is_active_uk',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Page.is_active_ru'
        db.add_column(u'site_page', 'is_active_ru',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Page.is_active_en'
        db.add_column(u'site_page', 'is_active_en',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'TopSlider.language'
        db.add_column(u'site_topslider', 'language',
                      self.gf('django.db.models.fields.CharField')(default='uk', max_length=8),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ClientQuote.title_uk'
        db.delete_column(u'site_clientquote', 'title_uk')

        # Deleting field 'ClientQuote.title_ru'
        db.delete_column(u'site_clientquote', 'title_ru')

        # Deleting field 'ClientQuote.title_en'
        db.delete_column(u'site_clientquote', 'title_en')

        # Deleting field 'ClientQuote.text_uk'
        db.delete_column(u'site_clientquote', 'text_uk')

        # Deleting field 'ClientQuote.text_ru'
        db.delete_column(u'site_clientquote', 'text_ru')

        # Deleting field 'ClientQuote.text_en'
        db.delete_column(u'site_clientquote', 'text_en')

        # Deleting field 'ClientQuote.is_active_uk'
        db.delete_column(u'site_clientquote', 'is_active_uk')

        # Deleting field 'ClientQuote.is_active_ru'
        db.delete_column(u'site_clientquote', 'is_active_ru')

        # Deleting field 'ClientQuote.is_active_en'
        db.delete_column(u'site_clientquote', 'is_active_en')

        # Deleting field 'Page.title_uk'
        db.delete_column(u'site_page', 'title_uk')

        # Deleting field 'Page.title_ru'
        db.delete_column(u'site_page', 'title_ru')

        # Deleting field 'Page.title_en'
        db.delete_column(u'site_page', 'title_en')

        # Deleting field 'Page.text_uk'
        db.delete_column(u'site_page', 'text_uk')

        # Deleting field 'Page.text_ru'
        db.delete_column(u'site_page', 'text_ru')

        # Deleting field 'Page.text_en'
        db.delete_column(u'site_page', 'text_en')

        # Deleting field 'Page.short_text_uk'
        db.delete_column(u'site_page', 'short_text_uk')

        # Deleting field 'Page.short_text_ru'
        db.delete_column(u'site_page', 'short_text_ru')

        # Deleting field 'Page.short_text_en'
        db.delete_column(u'site_page', 'short_text_en')

        # Deleting field 'Page.is_active_uk'
        db.delete_column(u'site_page', 'is_active_uk')

        # Deleting field 'Page.is_active_ru'
        db.delete_column(u'site_page', 'is_active_ru')

        # Deleting field 'Page.is_active_en'
        db.delete_column(u'site_page', 'is_active_en')

        # Deleting field 'TopSlider.language'
        db.delete_column(u'site_topslider', 'language')


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
            'Meta': {'object_name': 'Page'},
            'category': ('django.db.models.fields.IntegerField', [], {'default': '2', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_en': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_ru': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_uk': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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