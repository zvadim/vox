# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m


class PublicationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('create_date', 'title', 'category')
    list_display_links = ('title',)
    radio_fields = {"category": admin.VERTICAL}


admin.site.register(m.Publication, PublicationAdmin)