# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m
from django import forms
from tinymce.widgets import TinyMCE


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = m.Page
        widgets = {
            'text': TinyMCE(attrs={'cols': 90, 'rows': 30},),
        }


class PageAdmin(admin.ModelAdmin):
    radio_fields = {"category": admin.VERTICAL}
    prepopulated_fields = {"slug": ("title",)}
    form = PageAdminForm

    def get_prepopulated_fields(self, request, obj=None):
        if obj is not None:
            return {}
        return self.prepopulated_fields

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['slug']
        return []


class ClientAdmin(admin.ModelAdmin):
    pass


class ClientQuoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(m.Page, PageAdmin)
admin.site.register(m.Client, ClientAdmin)
admin.site.register(m.ClientQuote, ClientQuoteAdmin)