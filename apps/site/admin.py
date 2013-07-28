# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    radio_fields = {"category": admin.VERTICAL}


admin.site.register(m.Page, PageAdmin)