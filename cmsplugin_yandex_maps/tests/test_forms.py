from django.test import TestCase
from cmsplugin_yandex_maps.forms import *

class YandexMapsFormTestCase(TestCase):
    def setUp(self):
        self.form_data = {'title': 'YandexMapsFormTestCase', 'map_type': 'map', 'lang': 'ru_RU',
                     'auto_placement': True, 'zoom': 12, 'min_zoom': 0, 'max_zoom': 23,
                     'center_lt': 55.76, 'center_lg': 37.64, 'sizing': 'aspect', 'width': 320,
                     'height': 180, 'size_update_method': '', 'jq_selector': '', 'jq_event': 'click',
                     'behaviors': (1, 2, 3, 4, 6), 'controls': (5, 6, 7), 'classes': '',
                     'placemarks': '', 'collections': '', 'clasters': '', 'routes': ''}

    def test_form_is_valid(self):
        form = YandexMapsForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_clean_jq_selector(self):
        form_data = self.form_data
        
        form_data.update({'jq_selector': "quotes 'in' selector"})
        form = YandexMapsForm(data=form_data)
        form.is_valid()
        cleaned_data = form.clean_jq_selector()
        self.assertEqual(cleaned_data, "quotes 'in' selector")

        form_data.update({'jq_selector': 'double quotes "in" selector'})
        form = YandexMapsForm(data=form_data)
        form.is_valid()
        cleaned_data = form.clean_jq_selector()
        self.assertEqual(cleaned_data, "double quotes 'in' selector")

        form_data.update({'jq_selector': "'strip ' in selector'"})
        form = YandexMapsForm(data=form_data)
        form.is_valid()
        cleaned_data = form.clean_jq_selector()
        self.assertEqual(cleaned_data, "strip ' in selector")

        form_data.update({'jq_selector': '"strip " in selector"'})
        form = YandexMapsForm(data=form_data)
        form.is_valid()
        cleaned_data = form.clean_jq_selector()
        self.assertEqual(cleaned_data, "strip ' in selector")

        form_data.update({'jq_selector': " strip ' ' in selector "})
        form = YandexMapsForm(data=form_data)
        form.is_valid()
        cleaned_data = form.clean_jq_selector()
        self.assertEqual(cleaned_data, "strip ' ' in selector")

        form_data.update({'jq_selector': '''' " strip "mix" in selector "' '''})
        form = YandexMapsForm(data=form_data)
        form.is_valid()
        cleaned_data = form.clean_jq_selector()
        self.assertEqual(cleaned_data, "strip 'mix' in selector")


class PlacemarkFormTestCase(TestCase):
    def setUp(self):
        self.form_data = {'title': 'PlacemarkFormTestCase', 'auto_coordinates': True, 'place': 'Home',
                          'auto_placement': True, 'place_lt': None, 'place_lg': None,
                          'icon_style': 'default', 'icon_color': 'red', 'icon_circle': False,
                          'icon_caption': False, 'icon_glif': 'Home', 'icon_image': '',
                          'icon_width': 30, 'icon_height': 30, 'icon_offset_horizontal': 0,
                          'icon_offset_vertical': 0, 'icon_content_offset_horizontal': 0,
                          'icon_content_offset_vertical': 0, 'hint': '', 'balloon': '',
                          'balloonHeader': '', 'balloonBody': '', 'balloonFooter': '',
                          'point_type': 'wayPoint'}

    def test_form_is_valid(self):
        form = PlacemarkForm(data=self.form_data)
        self.assertTrue(form.is_valid())


class CollectionFormTestCase(TestCase):
    def setUp(self):
        self.form_data = {'title': 'CollectionFormTestCase', 'placemarks': '', 'icon_style': '',
                          'icon_color': '', 'icon_circle': False, 'icon_caption': False,
                          'icon_glif': 'Home', 'icon_image': '', 'icon_width': 30, 'icon_height': 30,
                          'icon_offset_horizontal': 0,
                          'icon_offset_vertical': 0, 'icon_content_offset_horizontal': 0,
                          'icon_content_offset_vertical': 0, 'hint': '', 'balloon': ''}

    def test_form_is_valid(self):
        form = CollectionForm(data=self.form_data)
        self.assertTrue(form.is_valid())


class ClasterFormTestCase(TestCase):
    def setUp(self):
        self.form_data = {'title': 'ClasterFormTestCase', 'placemarks': '', 'icon_style': '',
                          'icon_color': '', 'icon_circle': False, 'icon_caption': False,
                          'icon_glif': 'Home', 'icon_image': '', 'icon_width': 30, 'icon_height': 30,
                          'icon_offset_horizontal': 0,
                          'icon_offset_vertical': 0, 'icon_content_offset_horizontal': 0,
                          'icon_content_offset_vertical': 0, 'hint': '', 'balloon': '',
                          'disable_click_zoom': True, 'cluster_icon': 'default', 'cluster_color': 'red'}

    def test_form_is_valid(self):
        form = ClasterForm(data=self.form_data)
        self.assertTrue(form.is_valid())


class RouteFormTestCase(TestCase):
    def setUp(self):
        self.form_data = {'title': 'RouteFormTestCase', 'placemarks': '', 'routing_mode': 'auto',
                          'avoid_traffic_jams': False, 'results': 1, 'route_collor': '#9635ba',
                          'additional_routes_collor': '#7a684e'}

    def test_form_is_valid(self):
        form = RouteForm(data=self.form_data)
        form.is_valid()
        self.assertEqual(len(form.errors['__all__']), 1)
        self.assertIn("To create route need at least two Placemarks", form.errors['__all__'])