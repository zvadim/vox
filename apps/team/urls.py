from django.conf.urls import patterns, url

urlpatterns = patterns('apps.team.views',
    url(r'^ajax/get_member/(?P<pk>[0-9]+)/$', 'get_member', name='team_get_member'),
)
