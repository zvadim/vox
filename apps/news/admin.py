# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m
from django import forms
from tinymce.widgets import TinyMCE
from advanced_imagefield.admin import AdvancedImageInline
from modeltranslation.admin import TranslationAdmin


class PublicationAdminForm(forms.ModelForm):
    class Meta:
        model = m.Publication
        widgets = {
            'text_uk': TinyMCE(attrs={'cols': 90, 'rows': 30},),
            'text_ru': TinyMCE(attrs={'cols': 90, 'rows': 30},),
            'text_en': TinyMCE(attrs={'cols': 90, 'rows': 30},),
        }


class PublicationAdmin(TranslationAdmin):
    fieldsets = [
        (u'Content', {'fields': ('title', 'short_text', 'text', 'is_active')}),
        (None, {'fields': ('slug', 'create_date', 'category', 'image')}),
    ]

    prepopulated_fields = {"slug": ("title",)}
    list_display = ('create_date', 'title', 'category', 'is_active')
    list_display_links = ('title',)
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'short_text', 'text')
    radio_fields = {"category": admin.VERTICAL}
    form = PublicationAdminForm
    inlines = [AdvancedImageInline]

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(m.Publication, PublicationAdmin)