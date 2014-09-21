from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

if settings.USE_I18N:
    ptrn = i18n_patterns
else:
    ptrn = patterns

urlpatterns = ptrn('',
    url(r'^', include('apps.{{project_name}}.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # urls here
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^browse-api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
