# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m
from django import forms
from tinymce.widgets import TinyMCE
from modeltranslation.admin import TranslationAdmin


class MemberAdminForm(forms.ModelForm):
    class Meta:
        model = m.Member
        widgets = {
            'about_uk': TinyMCE(attrs={'cols': 90, 'rows': 30},),
            'about_ru': TinyMCE(attrs={'cols': 90, 'rows': 30},),
            'about_en': TinyMCE(attrs={'cols': 90, 'rows': 30},),
        }


class MemberAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'position', 'is_active')
    form = MemberAdminForm

    fieldsets = [
        (u'Content', {'fields': ('name', 'position', 'about')}),
        (None, {'fields': ('slug', 'email', 'tel', 'photo', 'is_active')}),
    ]

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class PublicationAdminForm(forms.ModelForm):
    class Meta:
        model = m.Publication
        widgets = {
            'text_uk': TinyMCE(attrs={'cols': 90, 'rows': 30},),
            'text_ru': TinyMCE(attrs={'cols': 90, 'rows': 30},),
            'text_en': TinyMCE(attrs={'cols': 90, 'rows': 30},),
        }


class PublicationAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'author', 'category', 'is_active')
    list_filter = ('title', 'author', 'category', 'is_active')
    search_fields = ('title', 'text')
    form = PublicationAdminForm

    fieldsets = [
        (u'Content', {'fields': ('title', 'short_text', 'text', 'is_active')}),
        (None, {'fields': ('slug', 'category', 'author', 'image', 'create_date')}),
    ]

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class CategoryAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'is_active')

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(m.Member, MemberAdmin)
admin.site.register(m.Publication, PublicationAdmin)
admin.site.register(m.Category, CategoryAdmin)