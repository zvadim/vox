from django.conf.urls import patterns, url
from .models import Page

urlpatterns = patterns('apps.site.views',
    url(r'^$', 'main', name='main'),
    url(r'^practice/(?P<slug>.*)/$', 'generic_page', name='site_page_%s' % Page.C_PR),
    url(r'^industry/(?P<slug>.*)/$', 'generic_page', name='site_page_%s' % Page.C_IND),
    url(r'^page/(?P<slug>.*)/$', 'generic_page', name='site_page_%s' % Page.C_PAGE),
)
