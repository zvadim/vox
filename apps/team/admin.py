# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m


class MemberAdmin(admin.ModelAdmin):
    pass


class PublicationAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(m.Member, MemberAdmin)
admin.site.register(m.Publication, PublicationAdmin)
admin.site.register(m.Category, CategoryAdmin)