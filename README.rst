=====================
cmsplugin-yandex-maps
=====================

Rich functionality Yandex Maps plugin for Django-CMS

.. image:: https://img.shields.io/badge/Donate-PayPal-blue.svg
   :target: https://www.paypal.me/Atterratio
.. image:: https://img.shields.io/badge/Donate-YaMoney-orange.svg
   :target: http://yasobe.ru/na/atterratio


------
v0.4.2
------

INSTALLATION
============

* `pip install cmsplugin-yandex-map` or `pip install git+https://github.com/Atterratio/cmsplugin-yandex-maps.git`;
* add `cmsplugin-yandex-map` to your `INSTALLED_APPS`;
* run `manage.py migrate`;
* run `manage.py collectstatic`;
* add `jQuery` to you page template if you haven't do this already;
- (optional) for "drag & drop" map and marker add `url(r'^yamaps/', include('cmsplugin_yandex_maps.urls', namespace="yamaps")),` to yours `urlpatterns` in `urls.py`, or add app `Yandex Maps` to one of you pages.


FEATURES
========

* map & markers customisation
* several maps on page
* multi markers
* auto coordinates and auto placment
* "drag & drop" markers and map(in page edit mode)
* standalone marker simple(right click on map in page edit mode) create
* size tweak
* hack for hidden ellements like modal, accordion, carousel
* routing


CHANGELOG
=========

v0.4.2:
-------

* fix save placement button icon
* fix README

v0.4.1:
-------

* return README.rst for divio support
* remove LANGUAGE_CODE from template(unnecessary can do bugs)

v0.4.0:
-------

* remove jQuery from plugin template(see instalation)
* change map placment from page edit mod
* "drag & drop" placemarks from page edit mod
* add standalone placemark by right click on map in page edit mod


v0.3.0:
-------

* improved clusterisation
* improved routing
* add collections


v0.2.1:
-------

* fix not copy markers on page save


v0.2.0:
-------

* now can add one marker to many maps


v0.1.1:
-------

* fix crash on set place latitude and longitude
* fix not blank Behaviors and Controls
