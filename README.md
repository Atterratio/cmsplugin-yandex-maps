cmsplugin-yandex-maps
===========
Rich functionality Yandex Maps plugin for Django-CMS


v0.4.0
-------

Rich functionality Yandex Maps plugin for Django-CMS


INSTALLATION
===========

`pip install cmsplugin-yandex-map`

or

`pip install git+https://github.com/Atterratio/cmsplugin-yandex-maps.git`

Then, add `cmsplugin-yandex-map` to your `INSTALLED_APPS` and run `manage.py migrate`.

Add "jQuery" to you page template if you have't do this already.

Add `url(r'^yamaps/', include('cmsplugin_yandex_maps.urls', namespace="yamaps")),` to yours `urlpatterns`, or add `Apphook` to some page, for more simplest map and placemarks placement changing. Don't forgot about permissions!

FEATURES
===========

* map & markers customisation
* several maps on page
* multi markers
* auto coordinates and auto placment
* "drag & drop" coordinates receipt
* size tweak
* hack for hidden ellements like modal, accordion, carousel
* routing


Changelog
-------
####v0.4.0
* remove jQuery from plugin template(see instalation)
* change map placment from page edit mod
* "drag & drop" placemarks from page edit mod
* add standalone placemark by right click on map in page edit mod


####v0.3.0
* improved clusterisation
* improved routing
* add collections


####v0.2.1
* fix not copy markers on page save


####v0.2.0:
* now can add one marker to many maps


####v0.1.1:
* fix crash on set place latitude and longitude
* fix not blank Behaviors and Controls
