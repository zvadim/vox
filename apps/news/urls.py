from django.conf.urls import patterns, url

urlpatterns = patterns('apps.news.views',
    url(r'^news/$', 'news_list', name='news_list'),
    url(r'^news/(?P<slug>.*)/$', 'news_item', name='news_item'),
    url(r'^publications/$', 'publication_list', name='articles_list'),
    url(r'^publication/(?P<slug>.*)/$', 'publication_item', name='articles_item'),
)
