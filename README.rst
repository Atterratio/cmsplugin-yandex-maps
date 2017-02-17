cmsplugin-yandex-maps
===========
Rich functionality Yandex Maps plugin for Django-CMS


v0.3.0
-------

Rich functionality Yandex Maps plugin for Django-CMS


INSTALLATION
===========

`pip install cmsplugin-yandex-map`

or

`pip install git+https://github.com/Atterratio/cmsplugin-yandex-maps.git`

Then, add `cmsplugin-yandex-map` to your `INSTALLED_APPS` and run `manage.py migrate`.


FEATURES
===========

* map & markers customisation
* several maps on page
* multi markers
* auto coordinates and auto placment
* size tweak
* hack for hidden ellements like modal, accordion, carousel
* routing(ugly)


Changelog
-------
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
