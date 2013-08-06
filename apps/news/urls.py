from django.conf.urls import patterns, url

urlpatterns = patterns('apps.news.views',
    url(r'^news/$', 'news_list', name='news_list'),
    url(r'^events/$', 'events_list', name='news_events_list'),
    url(r'^c/(?P<type>[a-z]+)/(?P<slug>.+)/$', 'publication_item', name='news_publication_item'),
)
