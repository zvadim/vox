# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m
from django import forms
from tinymce.widgets import TinyMCE


class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'position', 'is_active')


class PublicationAdminForm(forms.ModelForm):
    class Meta:
        model = m.Publication
        widgets = {
            'text': TinyMCE(attrs={'cols': 90, 'rows': 30},),
        }


class PublicationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'author', 'category', 'is_active')
    list_filter = ('title', 'author', 'category', 'is_active')
    search_fields = ('title', 'text')
    form = PublicationAdminForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'is_interview', 'is_active')


admin.site.register(m.Member, MemberAdmin)
admin.site.register(m.Publication, PublicationAdmin)
admin.site.register(m.Category, CategoryAdmin)