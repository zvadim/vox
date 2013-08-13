# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m
from django import forms
from tinymce.widgets import TinyMCE
from modeltranslation.admin import TranslationAdmin


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = m.Page
        widgets = {
            'text_uk': TinyMCE(attrs={'cols': 90, 'rows': 30},),
            'text_ru': TinyMCE(attrs={'cols': 90, 'rows': 30},),
            'text_en': TinyMCE(attrs={'cols': 90, 'rows': 30},),
        }


class PageAdmin(TranslationAdmin):
    radio_fields = {"category": admin.VERTICAL}
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('category', 'is_active')
    list_display = ('title', 'category', 'is_active')
    search_fields = ('title', 'short_text', 'text')
    form = PageAdminForm

    fieldsets = [
        (u'Content', {'fields': ('title', 'short_text', 'text', 'is_active')}),
        (None, {'fields': ('slug', 'category', 'image')}),
    ]

    def get_prepopulated_fields(self, request, obj=None):
        if obj is not None:
            return {}
        return self.prepopulated_fields

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['slug']
        return []

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ClientAdmin(admin.ModelAdmin):
    pass


class ClientQuoteAdmin(TranslationAdmin):
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class TopSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'is_active', 'url')
    list_filter = ('language', 'is_active')

admin.site.register(m.TopSlider, TopSliderAdmin)
admin.site.register(m.Page, PageAdmin)
admin.site.register(m.Client, ClientAdmin)
admin.site.register(m.ClientQuote, ClientQuoteAdmin)