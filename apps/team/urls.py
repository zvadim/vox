from django.conf.urls import patterns, url

urlpatterns = patterns('apps.team.views',
    url(r'^ajax/get_member/(?P<pk>[0-9]+)/$', 'get_member', name='team_get_member'),
    url(r'^publication/(?P<slug>.+)/$', 'generic_page', name='team_publication_item'),
    url(r'^publications/$', 'publication_list', name='team_articles_list'),
    url(r'^publications/(?P<slug>.+)/$', 'publication_list', name='team_articles_cat_list'),

)
