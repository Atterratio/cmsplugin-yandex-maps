from django.conf.urls import include, url
import cmsplugin_yandex_maps.urls


urlpatterns = (
    url(r'^yamaps/', include(cmsplugin_yandex_maps.urls, namespace='yamaps')),
)