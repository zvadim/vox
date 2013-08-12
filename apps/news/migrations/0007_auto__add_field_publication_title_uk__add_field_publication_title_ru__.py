# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Publication.title_uk'
        db.add_column(u'news_publication', 'title_uk',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.title_ru'
        db.add_column(u'news_publication', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.title_en'
        db.add_column(u'news_publication', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.short_text_uk'
        db.add_column(u'news_publication', 'short_text_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.short_text_ru'
        db.add_column(u'news_publication', 'short_text_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.short_text_en'
        db.add_column(u'news_publication', 'short_text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.text_uk'
        db.add_column(u'news_publication', 'text_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.text_ru'
        db.add_column(u'news_publication', 'text_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.text_en'
        db.add_column(u'news_publication', 'text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.is_active_uk'
        db.add_column(u'news_publication', 'is_active_uk',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Publication.is_active_ru'
        db.add_column(u'news_publication', 'is_active_ru',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Publication.is_active_en'
        db.add_column(u'news_publication', 'is_active_en',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Publication.title_uk'
        db.delete_column(u'news_publication', 'title_uk')

        # Deleting field 'Publication.title_ru'
        db.delete_column(u'news_publication', 'title_ru')

        # Deleting field 'Publication.title_en'
        db.delete_column(u'news_publication', 'title_en')

        # Deleting field 'Publication.short_text_uk'
        db.delete_column(u'news_publication', 'short_text_uk')

        # Deleting field 'Publication.short_text_ru'
        db.delete_column(u'news_publication', 'short_text_ru')

        # Deleting field 'Publication.short_text_en'
        db.delete_column(u'news_publication', 'short_text_en')

        # Deleting field 'Publication.text_uk'
        db.delete_column(u'news_publication', 'text_uk')

        # Deleting field 'Publication.text_ru'
        db.delete_column(u'news_publication', 'text_ru')

        # Deleting field 'Publication.text_en'
        db.delete_column(u'news_publication', 'text_en')

        # Deleting field 'Publication.is_active_uk'
        db.delete_column(u'news_publication', 'is_active_uk')

        # Deleting field 'Publication.is_active_ru'
        db.delete_column(u'news_publication', 'is_active_ru')

        # Deleting field 'Publication.is_active_en'
        db.delete_column(u'news_publication', 'is_active_en')


    models = {
        u'advanced_imagefield.advancedimage': {
            'Meta': {'object_name': 'AdvancedImage'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('advanced_imagefield.fields.AdvancedImageField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'news.publication': {
            'Meta': {'ordering': "['-create_date', '-pk']", 'object_name': 'Publication'},
            'category': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 12, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_en': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_ru': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active_uk': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'short_text': ('django.db.models.fields.TextField', [], {}),
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
        }
    }

    complete_apps = ['news']