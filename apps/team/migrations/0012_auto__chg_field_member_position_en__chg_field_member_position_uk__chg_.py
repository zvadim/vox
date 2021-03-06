# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Member.position_en'
        db.alter_column(u'team_member', 'position_en', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'Member.position_uk'
        db.alter_column(u'team_member', 'position_uk', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'Member.position'
        db.alter_column(u'team_member', 'position', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Member.position_ru'
        db.alter_column(u'team_member', 'position_ru', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

    def backwards(self, orm):

        # Changing field 'Member.position_en'
        db.alter_column(u'team_member', 'position_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Member.position_uk'
        db.alter_column(u'team_member', 'position_uk', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Member.position'
        db.alter_column(u'team_member', 'position', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'Member.position_ru'
        db.alter_column(u'team_member', 'position_ru', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

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
            'position': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'position_en': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'position_ru': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'position_uk': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'team.publication': {
            'Meta': {'object_name': 'Publication'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Member']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Category']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 14, 0, 0)'}),
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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['team']