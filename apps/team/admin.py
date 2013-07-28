# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m


class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PublicationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(m.Member, MemberAdmin)
admin.site.register(m.Publication, PublicationAdmin)
admin.site.register(m.Category, CategoryAdmin)