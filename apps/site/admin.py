# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    radio_fields = {"category": admin.VERTICAL}


class ClientAdmin(admin.ModelAdmin):
    pass


class ClientQuoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(m.Page, PageAdmin)
admin.site.register(m.Client, ClientAdmin)
admin.site.register(m.ClientQuote, ClientQuoteAdmin)