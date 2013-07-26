# -*- coding: UTF-8 -*-
from django.contrib import admin
from . import models as m


class TeamAdmin(admin.ModelAdmin):
    class Meta:
        model = m.Team

admin.site.register(m.Team, TeamAdmin)


class PublicationAdmin(admin.ModelAdmin):
    class Meta:
        model = m.Publication

admin.site.register(m.Publication, PublicationAdmin)