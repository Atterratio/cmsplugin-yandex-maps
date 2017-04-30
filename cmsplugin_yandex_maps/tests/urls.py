# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
import django.views
import cmsplugin_yandex_maps.urls

admin.autodiscover()


urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^yamaps/', include(cmsplugin_yandex_maps.urls, namespace='yamaps')),
    url(r'^', include('cms.urls')),
    url(r'^media/(?P<path>.*)$', django.views.static.serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)