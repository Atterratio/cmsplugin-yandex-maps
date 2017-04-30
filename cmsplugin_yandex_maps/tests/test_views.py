import os

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

import cms.api

from cmsplugin_yandex_maps.cms_plugins import YandexMapsPlugin
from cmsplugin_yandex_maps.models import YandexMaps, Placemark

try:
    DJANGO_VERSION = os.environ['DJANGO_VERSION']
except:
    DJANGO_VERSION = "1.10.*"



class ViewsTestCase(TestCase):
    def setUp(self):
        self.anon_client = Client()

        self.admin_client = Client()

        self.test_admin = User.objects.create_superuser('admin', 'admin@test', 'admin')

        if DJANGO_VERSION == "1.8.*":
            self.admin_client.login(username='admin', password='admin')
        else:
            self.admin_client.force_login(self.test_admin)


    def test_no_perm(self):
        resp = self.anon_client.post('/yamaps/ajax/update/placement/')

        self.assertEqual(resp.status_code, 403)


        resp = self.anon_client.post('/yamaps/ajax/update/placemark/')

        self.assertEqual(resp.status_code, 403)


    def test_update_placement(self):
        test_page = cms.api.create_page('Test Page', 'base.html', 'en')

        test_placeholder = test_page.placeholders.get(slot='test')

        test_map_data = {'title': 'Test map', 'map_type': 'map', 'lang': 'ru_RU',
                     'auto_placement': True, 'zoom': 11, 'min_zoom': 0, 'max_zoom': 23,
                     'center_lt': 55.76, 'center_lg': 37.64, 'sizing': 'auto', 'width': 320,
                     'height': 180, 'size_update_method': '', 'jq_selector': '', 'jq_event': 'click',
                     'behaviors': (1, 2, 3, 4, 6), 'controls': (5, 6, 7), 'classes': '',
                     'placemarks': '', 'collections': '', 'clasters': '', 'routes': ''}
        test_map_plugin = cms.api.add_plugin(test_placeholder, YandexMapsPlugin, 'en')
        test_map_plugin.__dict__.update(test_map_data)
        test_map_plugin.save()

        data = '{"id": "1", "center": [50, 35], "zoom": 10}'
        resp = self.admin_client.post('/yamaps/ajax/update/placement/', data, 'json')

        test_map = YandexMaps.objects.get(id=1)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(test_map.center_lt, 50)
        self.assertEqual(test_map.center_lg, 35)
        self.assertEqual(test_map.zoom, 10)


    def test_update_placemark(self):
        test_placemark_data = {'title': 'Test Placemark', 'auto_coordinates': True, 'place': 'Home',
                          'auto_placement': True, 'place_lt': None, 'place_lg': None,
                          'icon_style': 'default', 'icon_color': 'red', 'icon_circle': False,
                          'icon_caption': False, 'icon_glif': 'Home', 'icon_image': '',
                          'icon_width': 30, 'icon_height': 30, 'icon_offset_horizontal': 0,
                          'icon_offset_vertical': 0, 'icon_content_offset_horizontal': 0,
                          'icon_content_offset_vertical': 0, 'hint': '', 'balloon': '',
                          'balloonHeader': '', 'balloonBody': '', 'balloonFooter': '',
                          'point_type': 'wayPoint'}
        test_placemark = Placemark()
        test_placemark.__dict__.update(test_placemark_data)
        test_placemark.save()

        data = '{"id": 1, "position": [10, 20]}'
        resp = self.admin_client.post('/yamaps/ajax/update/placemark/', data, 'json')

        test_placemark_updated = Placemark.objects.get(id=1)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(test_placemark_updated.place_lt, 10)
        self.assertEqual(test_placemark_updated.place_lg, 20)
        self.assertEqual(test_placemark_updated.auto_coordinates, False)