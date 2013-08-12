from django.conf.urls.static import static
from django.conf.urls import patterns, url, include
from solid_i18n.urls import solid_i18n_patterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = solid_i18n_patterns('',
    url(r'^member/', include('apps.team.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^', include('apps.site.urls')),
    url(r'^', include('apps.news.urls')),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

if 'tinymce' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^tinymce/', include('tinymce.urls')),
        url(r'^tinymce/filebrowser/', include('filebrowser.urls')),
    )
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

# For development only
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
    )
