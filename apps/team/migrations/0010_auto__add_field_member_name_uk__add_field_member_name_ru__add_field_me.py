# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Member.name_uk'
        db.add_column(u'team_member', 'name_uk',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Member.name_ru'
        db.add_column(u'team_member', 'name_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Member.name_en'
        db.add_column(u'team_member', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Member.position_uk'
        db.add_column(u'team_member', 'position_uk',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Member.position_ru'
        db.add_column(u'team_member', 'position_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Member.position_en'
        db.add_column(u'team_member', 'position_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Member.about_uk'
        db.add_column(u'team_member', 'about_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Member.about_ru'
        db.add_column(u'team_member', 'about_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Member.about_en'
        db.add_column(u'team_member', 'about_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.title_uk'
        db.add_column(u'team_category', 'title_uk',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.title_ru'
        db.add_column(u'team_category', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.title_en'
        db.add_column(u'team_category', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.title_uk'
        db.add_column(u'team_publication', 'title_uk',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.title_ru'
        db.add_column(u'team_publication', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.title_en'
        db.add_column(u'team_publication', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.short_text_uk'
        db.add_column(u'team_publication', 'short_text_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.short_text_ru'
        db.add_column(u'team_publication', 'short_text_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.short_text_en'
        db.add_column(u'team_publication', 'short_text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.text_uk'
        db.add_column(u'team_publication', 'text_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.text_ru'
        db.add_column(u'team_publication', 'text_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.text_en'
        db.add_column(u'team_publication', 'text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Publication.is_active_uk'
        db.add_column(u'team_publication', 'is_active_uk',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Publication.is_active_ru'
        db.add_column(u'team_publication', 'is_active_ru',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Publication.is_active_en'
        db.add_column(u'team_publication', 'is_active_en',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Member.name_uk'
        db.delete_column(u'team_member', 'name_uk')

        # Deleting field 'Member.name_ru'
        db.delete_column(u'team_member', 'name_ru')

        # Deleting field 'Member.name_en'
        db.delete_column(u'team_member', 'name_en')

        # Deleting field 'Member.position_uk'
        db.delete_column(u'team_member', 'position_uk')

        # Deleting field 'Member.position_ru'
        db.delete_column(u'team_member', 'position_ru')

        # Deleting field 'Member.position_en'
        db.delete_column(u'team_member', 'position_en')

        # Deleting field 'Member.about_uk'
        db.delete_column(u'team_member', 'about_uk')

        # Deleting field 'Member.about_ru'
        db.delete_column(u'team_member', 'about_ru')

        # Deleting field 'Member.about_en'
        db.delete_column(u'team_member', 'about_en')

        # Deleting field 'Category.title_uk'
        db.delete_column(u'team_category', 'title_uk')

        # Deleting field 'Category.title_ru'
        db.delete_column(u'team_category', 'title_ru')

        # Deleting field 'Category.title_en'
        db.delete_column(u'team_category', 'title_en')

        # Deleting field 'Publication.title_uk'
        db.delete_column(u'team_publication', 'title_uk')

        # Deleting field 'Publication.title_ru'
        db.delete_column(u'team_publication', 'title_ru')

        # Deleting field 'Publication.title_en'
        db.delete_column(u'team_publication', 'title_en')

        # Deleting field 'Publication.short_text_uk'
        db.delete_column(u'team_publication', 'short_text_uk')

        # Deleting field 'Publication.short_text_ru'
        db.delete_column(u'team_publication', 'short_text_ru')

        # Deleting field 'Publication.short_text_en'
        db.delete_column(u'team_publication', 'short_text_en')

        # Deleting field 'Publication.text_uk'
        db.delete_column(u'team_publication', 'text_uk')

        # Deleting field 'Publication.text_ru'
        db.delete_column(u'team_publication', 'text_ru')

        # Deleting field 'Publication.text_en'
        db.delete_column(u'team_publication', 'text_en')

        # Deleting field 'Publication.is_active_uk'
        db.delete_column(u'team_publication', 'is_active_uk')

        # Deleting field 'Publication.is_active_ru'
        db.delete_column(u'team_publication', 'is_active_ru')

        # Deleting field 'Publication.is_active_en'
        db.delete_column(u'team_publication', 'is_active_en')


    models = {
        u'team.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'team.member': {
            'Meta': {'object_name': 'Member'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'about_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'about_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'position_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'position_ru': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'position_uk': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'team.publication': {
            'Meta': {'object_name': 'Publication'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Member']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Category']"}),
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

    complete_apps = ['team']