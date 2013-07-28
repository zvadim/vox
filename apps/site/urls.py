from django.conf.urls import patterns, url

urlpatterns = patterns('apps.site.views',
    url(r'^$', 'main', name='main'),
)
