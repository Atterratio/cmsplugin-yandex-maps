.. image:: https://travis-ci.org/Atterratio/cmsplugin-yandex-maps.svg?branch=master
    :target: https://travis-ci.org/Atterratio/cmsplugin-yandex-maps
.. image:: https://codecov.io/gh/Atterratio/cmsplugin-yandex-maps/coverage.svg?branch=master
    :target: https://codecov.io/gh/Atterratio/cmsplugin-yandex-maps

=====================
cmsplugin-yandex-maps
=====================

Rich functionality Yandex Maps plugin for Django-CMS

.. image:: https://img.shields.io/badge/Donate-PayPal-blue.svg
   :target: https://www.paypal.me/Atterratio
.. image:: https://img.shields.io/badge/Donate-YaMoney-orange.svg
   :target: https://money.yandex.ru/to/410011005689134


------
v0.4.2
------

REQUIREMENTS
============

* *Python >= 3.3*
* *Django >= 1.8*
* *Django-CMS >=3.3*

INSTALLATION
============

* run :code:`pip install cmsplugin-yandex-map` or :code:`pip install git+https://github.com/Atterratio/cmsplugin-yandex-maps.git`;
* add :code:`cmsplugin-yandex-map` to your :code:`INSTALLED_APPS`;
* run :code:`manage.py migrate`;
* run :code:`manage.py collectstatic`;
* add *jQuery* to you page template if you haven't do this already;
* (optional) for "drag & drop" map and marker add :code:`import cmsplugin_yandex_maps.urls` and :code:`url(r'^yamaps/', include(cmsplugin_yandex_maps.urls, namespace="yamaps")),` to yours :code:`urlpatterns` in :code:`urls.py`, or add app *Yandex Maps* to one of you pages.


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