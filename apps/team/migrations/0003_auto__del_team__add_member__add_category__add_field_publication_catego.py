# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'team_team')

        # Adding model 'Member'
        db.create_table(u'team_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('about', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'team', ['Member'])

        # Adding model 'Category'
        db.create_table(u'team_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('is_vacancy', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'team', ['Category'])

        # Adding field 'Publication.category'
        db.add_column(u'team_publication', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['team.Category']),
                      keep_default=False)

        # Adding field 'Publication.slug'
        db.add_column(u'team_publication', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='1', max_length=50),
                      keep_default=False)


        # Changing field 'Publication.author'
        db.alter_column(u'team_publication', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Member']))

    def backwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'team_team', (
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'team', ['Team'])

        # Deleting model 'Member'
        db.delete_table(u'team_member')

        # Deleting model 'Category'
        db.delete_table(u'team_category')

        # Deleting field 'Publication.category'
        db.delete_column(u'team_publication', 'category_id')

        # Deleting field 'Publication.slug'
        db.delete_column(u'team_publication', 'slug')


        # Changing field 'Publication.author'
        db.alter_column(u'team_publication', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Team']))

    models = {
        u'team.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_vacancy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['team']