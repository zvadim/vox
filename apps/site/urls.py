from django.conf.urls import patterns, url
from rollyourown.seo.admin import register_seo_admin
from django.contrib import admin
from .seo import VoxMetadata

register_seo_admin(admin.site, VoxMetadata)

urlpatterns = patterns('apps.site.views',
    url(r'^$', 'main', name='main'),
    url(r'^get/(?P<type>[a-z]+)/(?P<slug>.*)/$', 'generic_page', name='site_page'),
)
