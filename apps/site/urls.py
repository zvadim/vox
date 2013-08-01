from django.conf.urls import patterns, url

urlpatterns = patterns('apps.site.views',
    url(r'^$', 'main', name='main'),
    url(r'^get/(?P<type>[a-z]+)/(?P<slug>.*)/$', 'generic_page', name='site_page'),
)
