from django.conf.urls import url

from cmsplugin_yandex_maps import views


app_name = 'yamaps'
urlpatterns = [
    url(r'^ajax/update/placement/$', views.update_placement, name='update_placement'),
    url(r'^ajax/update/placemark/$', views.update_placemark, name='update_placemark'),
]