from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
import cms.api
import os

from cmsplugin_yandex_maps.cms_plugins import YandexMapsPlugin
from cmsplugin_yandex_maps.models import Placemark, Collection, Claster, Route
from asyncore import write

try:
    CMS_VERSION = os.environ['CMS_VERSION']
except:
    CMS_VERSION = "3.4.*"

try:
    DJANGO_VERSION = os.environ['DJANGO_VERSION']
except:
    DJANGO_VERSION = "1.10.*"



class YandexMapsPluginTestCase(TestCase):
    def setUp(self):
        self.test_page = cms.api.create_page('Test Page', 'base.html', 'en')
        
        self.test_placeholder = self.test_page.placeholders.get(slot='test')
        
        test_map_data = {'title': 'Test map', 'map_type': 'map', 'lang': 'ru_RU',
                     'auto_placement': True, 'zoom': 11, 'min_zoom': 0, 'max_zoom': 23,
                     'center_lt': 55.76, 'center_lg': 37.64, 'sizing': 'auto', 'width': 320,
                     'height': 180, 'size_update_method': '', 'jq_selector': '', 'jq_event': 'click',
                     'behaviors': (1, 2, 3, 4, 6), 'controls': (5, 6, 7), 'classes': '',
                     'placemarks': '', 'collections': '', 'clasters': '', 'routes': ''}
        self.test_map = cms.api.add_plugin(self.test_placeholder, YandexMapsPlugin, 'en')
        self.test_map.__dict__.update(test_map_data)
        self.test_map.save()
        
        self.test_page.publish('en')
        
        self.draft_url = '{}?edit'.format(self.test_page.get_absolute_url('en'))
        self.public_url = '{}?edit_off'.format(self.test_page.get_absolute_url('en'))
        
        self.test_admin = User.objects.create_superuser('admin', 'admin@test', 'admin')
        
        self.client = Client()


    def test_draft_placement_edit(self):
        if DJANGO_VERSION == "1.8.*":
            self.client.login(username='admin', password='admin')
        else:
            self.client.force_login(self.test_admin)
            
        draft_html = bytes.decode(self.client.get(self.draft_url).content)
        self.assertIn('yaMap_{map}.controls.add(savePlacement_{map});'.
                      format(map=self.test_map.id), draft_html)


    def test_map_update_method(self):
        self.test_map.size_update_method = "observer"
        self.test_map.save()
         
        self.test_page.publish('en')
        
        public_test_page = self.test_page.get_public_object()
        public_test_placeholder = public_test_page.placeholders.get(slot='test')
        if CMS_VERSION == "3.4.*":
            public_test_map = public_test_placeholder.get_plugins_list()[0].get_bound_plugin()
        else:
            public_test_map = public_test_placeholder.get_plugins_list()[0].get_plugin_instance()[0]
        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('observer_{map}.observe(target_{map}, config_{map});'.
                      format(map=public_test_map.id), public_html)


        self.test_map.size_update_method = "jq_event"
        self.test_map.jq_event = "test_jq_event"
        self.test_map.save()

        self.test_page.publish('en')

        public_test_page = self.test_page.get_public_object()
        public_test_placeholder = public_test_page.placeholders.get(slot='test')
        if CMS_VERSION == "3.4.*":
            public_test_map = public_test_placeholder.get_plugins_list()[0].get_bound_plugin()
        else:
            public_test_map = public_test_placeholder.get_plugins_list()[0].get_plugin_instance()[0]
        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('$(document).on("{jq_event}"'.
                      format(jq_event=public_test_map.jq_event), public_html)


    def test_map_sizing(self):
        self.test_map.sizing = 'auto'
        self.test_map.save()

        self.test_page.publish('en')

        public_test_page = self.test_page.get_public_object()
        public_test_placeholder = public_test_page.placeholders.get(slot='test')
        if CMS_VERSION == "3.4.*":
            public_test_map = public_test_placeholder.get_plugins_list()[0].get_bound_plugin()
        else:
            public_test_map = public_test_placeholder.get_plugins_list()[0].get_plugin_instance()[0]
        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('''function ya_map_container_size_{map}(){{
    
        $('#map-{map}').parent().width('100%');
        var map_height = $('#map-{map}').parent().parent().parent().height();
        $('#map-{map}').parent().outerHeight(map_height, true);
    
}}'''.format(map=public_test_map.id), public_html)


        self.test_map.sizing = 'aspect'
        self.test_map.save()

        self.test_page.publish('en')

        public_test_page = self.test_page.get_public_object()
        public_test_placeholder = public_test_page.placeholders.get(slot='test')

        if CMS_VERSION == "3.4.*":
            public_test_map = public_test_placeholder.get_plugins_list()[0].get_bound_plugin()
        else:
            public_test_map = public_test_placeholder.get_plugins_list()[0].get_plugin_instance()[0]

        public_html = bytes.decode(self.client.get(self.public_url).content)

        self.assertIn('''function ya_map_container_size_{map}(){{
    
        $('#map-{map}').parent().width('100%');
        $('#map-{map}').parent().height($('#map-{map}').parent().width()/320*180);
    
}}'''.format(map=public_test_map.id), public_html)


        self.test_map.sizing = 'static'
        self.test_map.save()

        self.test_page.publish('en')

        public_test_page = self.test_page.get_public_object()
        public_test_placeholder = public_test_page.placeholders.get(slot='test')

        if CMS_VERSION == "3.4.*":
            public_test_map = public_test_placeholder.get_plugins_list()[0].get_bound_plugin()
        else:
            public_test_map = public_test_placeholder.get_plugins_list()[0].get_plugin_instance()[0]

        public_html = bytes.decode(self.client.get(self.public_url).content)

        self.assertIn('''function ya_map_container_size_{map}(){{
    
        $('#map-{map}').parent().width({width});
        $('#map-{map}').parent().height({height});
    
}}'''.format(map=public_test_map.id,
             width=public_test_map.width,
             height=public_test_map.height), public_html)



class PlacemarkPluginTestCase(TestCase):
    def setUp(self):
        self.test_page = cms.api.create_page('Test Page', 'base.html', 'en')
         
        test_placeholder = self.test_page.placeholders.get(slot='test')
         
        test_placemark_data = {'title': 'Test Placemark', 'auto_coordinates': True, 'place': 'Home',
                          'auto_placement': True, 'place_lt': None, 'place_lg': None,
                          'icon_style': 'default', 'icon_color': 'red', 'icon_circle': False,
                          'icon_caption': False, 'icon_glif': 'Home', 'icon_image': '',
                          'icon_width': 30, 'icon_height': 30, 'icon_offset_horizontal': 0,
                          'icon_offset_vertical': 0, 'icon_content_offset_horizontal': 0,
                          'icon_content_offset_vertical': 0, 'hint': '', 'balloon': '',
                          'balloonHeader': '', 'balloonBody': '', 'balloonFooter': '',
                          'point_type': 'wayPoint'}
        self.test_placemark = Placemark()
        self.test_placemark.__dict__.update(test_placemark_data)
        self.test_placemark.save()

        test_map_data = {'title': 'Test map', 'map_type': 'map', 'lang': 'ru_RU',
                     'auto_placement': True, 'zoom': 11, 'min_zoom': 0, 'max_zoom': 23,
                     'center_lt': 55.76, 'center_lg': 37.64, 'sizing': 'auto', 'width': 320,
                     'height': 180, 'size_update_method': '', 'jq_selector': '', 'jq_event': 'click',
                     'behaviors': (1, 2, 3, 4, 6), 'controls': (5, 6, 7), 'classes': '',
                     'placemarks': '', 'collections': '', 'clasters': '', 'routes': ''}
        test_map = cms.api.add_plugin(test_placeholder, YandexMapsPlugin, 'en')
        test_map.__dict__.update(test_map_data)
        test_map.placemarks.add(self.test_placemark)
        test_map.save()

        self.test_page.publish('en')

        public_test_page = self.test_page.get_public_object()
        public_test_placeholder = public_test_page.placeholders.get(slot='test')

        if CMS_VERSION == "3.4.*":
            self.public_test_map = public_test_placeholder.get_plugins_list()[0].get_bound_plugin()
        else:
            self.public_test_map = public_test_placeholder.get_plugins_list()[0].get_plugin_instance()[0]

        self.draft_url = '{}?edit'.format(self.test_page.get_absolute_url('en'))
        self.public_url = '{}?edit_off'.format(self.test_page.get_absolute_url('en'))

        self.test_admin = User.objects.create_superuser('admin', 'admin@test', 'admin')

        self.client = Client()


    def test_draft_draggable(self):
        if DJANGO_VERSION == "1.8.*":
            self.client.login(username='admin', password='admin')
        else:
            self.client.force_login(self.test_admin)

        draft_html = bytes.decode(self.client.get(self.draft_url).content)
        self.assertIn('draggable: true,', draft_html)

        self.test_placemark.auto_coordinates = False
        self.test_placemark.save()
        if DJANGO_VERSION == "1.8.*":
            self.client.login(username='admin', password='admin')
        else:
            self.client.force_login(self.test_admin)

        draft_html = bytes.decode(self.client.get(self.draft_url).content)
        self.assertIn('draggable: true,', draft_html)


    def test_style_default(self):
        self.test_placemark.style = 'default'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertRegex(public_html, 'iconContent: "\d+",')
        self.assertIn('preset: "islands#redIcon",', public_html)

        self.test_placemark.icon_color = 'blue'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blueIcon",', public_html)

        self.test_placemark.icon_circle = True
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blueCircleIcon",', public_html)


    def test_style_stretchy(self):
        self.test_placemark.icon_style = 'stretchy'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconContent: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn('preset: "islands#redStretchyIcon",', public_html)

        self.test_placemark.icon_color = 'darkOrange'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#darkOrangeStretchyIcon",', public_html)


    def test_style_doted(self):
        self.test_placemark.icon_style = 'doted'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#redDotIcon",', public_html)


        self.test_placemark.icon_color = 'black'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blackDotIcon",', public_html)


        self.test_placemark.icon_caption = True
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconCaption: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn('preset: "islands#blackDotIconWithCaption",', public_html)


        self.test_placemark.icon_circle = True
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconCaption: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn('preset: "islands#blackCircleDotIconWithCaption",', public_html)


        self.test_placemark.icon_caption = False
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blackCircleDotIcon",', public_html)


    def test_style_glif(self):
        self.test_placemark.icon_style = 'glif'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#redHomeIcon",', public_html)


        self.test_placemark.icon_color = 'violet'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#violetHomeIcon",', public_html)


        self.test_placemark.icon_glif = 'Cinema'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#violetCinemaIcon",', public_html)


        self.test_placemark.icon_circle = True
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#violetCinemaCircleIcon",', public_html)


    def test_style_image(self):
        self.test_placemark.icon_style = 'image'
        self.test_placemark.icon_image = 'Test Image'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn("iconLayout: 'default#image',", public_html)


        self.test_placemark.icon_caption = True
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconContent: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn("iconLayout: 'default#imageWithContent',", public_html)


    def test_hint(self):
        self.test_placemark.hint = 'Hint'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('hintContent: "Hint",', public_html)


    def test_balloon(self):
        self.test_placemark.balloon = 'Balloon'
        self.test_placemark.balloonHeader = 'Balloon Header'
        self.test_placemark.balloonBody = 'Balloon Body'
        self.test_placemark.balloonFooter = 'Balloon Footer'
        self.test_placemark.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('balloonContent: "Balloon",', public_html)
        self.assertIn("balloonContentHeader: 'Balloon Header',", public_html)
        self.assertIn("balloonContentBody: 'Balloon Body',", public_html)
        self.assertIn("balloonContentFooter: 'Balloon Footer',", public_html)


class CollectionTestCase(TestCase):
    def setUp(self):
        self.test_page = cms.api.create_page('Test Page', 'base.html', 'en')

        test_placeholder = self.test_page.placeholders.get(slot='test')

        test_collection_data = {'title': 'Test Collection', 'placemarks': '', 'icon_style': '',
                          'icon_color': 'red', 'icon_circle': False, 'icon_caption': False,
                          'icon_glif': 'Home', 'icon_image': '', 'icon_width': 30, 'icon_height': 30,
                          'icon_offset_horizontal': 0,
                          'icon_offset_vertical': 0, 'icon_content_offset_horizontal': 0,
                          'icon_content_offset_vertical': 0, 'hint': '', 'balloon': ''}
        self.test_collection = Collection()
        self.test_collection.__dict__.update(test_collection_data)
        self.test_collection.save()

        test_map_data = {'title': 'Test map', 'map_type': 'map', 'lang': 'ru_RU',
                     'auto_placement': True, 'zoom': 11, 'min_zoom': 0, 'max_zoom': 23,
                     'center_lt': 55.76, 'center_lg': 37.64, 'sizing': 'auto', 'width': 320,
                     'height': 180, 'size_update_method': '', 'jq_selector': '', 'jq_event': 'click',
                     'behaviors': (1, 2, 3, 4, 6), 'controls': (5, 6, 7), 'classes': '',
                     'placemarks': '', 'collections': '', 'clasters': '', 'routes': ''}
        test_map = cms.api.add_plugin(test_placeholder, YandexMapsPlugin, 'en')
        test_map.__dict__.update(test_map_data)
        test_map.save()

        test_placemark_data = {'title': 'Test Placemark', 'auto_coordinates': True, 'place': 'Home',
                          'auto_placement': True, 'place_lt': None, 'place_lg': None,
                          'icon_style': 'default', 'icon_color': 'red', 'icon_circle': False,
                          'icon_caption': False, 'icon_glif': 'Home', 'icon_image': '',
                          'icon_width': 30, 'icon_height': 30, 'icon_offset_horizontal': 0,
                          'icon_offset_vertical': 0, 'icon_content_offset_horizontal': 0,
                          'icon_content_offset_vertical': 0, 'hint': '', 'balloon': '',
                          'balloonHeader': '', 'balloonBody': '', 'balloonFooter': '',
                          'point_type': 'wayPoint'}
        self.test_placemark = Placemark()
        self.test_placemark.__dict__.update(test_placemark_data)
        self.test_placemark.save()

        self.test_collection.placemarks.add(self.test_placemark)
        self.test_collection.save()

        test_map.collections.add(self.test_collection)
        test_map.save()

        self.test_page.publish('en')

        public_test_page = self.test_page.get_public_object()
        public_test_placeholder = public_test_page.placeholders.get(slot='test')

        if CMS_VERSION == "3.4.*":
            self.public_test_map = public_test_placeholder.get_plugins_list()[0].get_bound_plugin()
        else:
            self.public_test_map = public_test_placeholder.get_plugins_list()[0].get_plugin_instance()[0]

        self.draft_url = '{}?edit'.format(self.test_page.get_absolute_url('en'))
        self.public_url = '{}?edit_off'.format(self.test_page.get_absolute_url('en'))

        self.test_admin = User.objects.create_superuser('admin', 'admin@test', 'admin')

        self.client = Client()


    def test_draft_draggable(self):
        if DJANGO_VERSION == "1.8.*":
            self.client.login(username='admin', password='admin')
        else:
            self.client.force_login(self.test_admin)

        draft_html = bytes.decode(self.client.get(self.draft_url).content)
        self.assertIn('draggable: true,', draft_html)

        self.test_placemark.auto_coordinates = False
        self.test_placemark.save()
        if DJANGO_VERSION == "1.8.*":
            self.client.login(username='admin', password='admin')
        else:
            self.client.force_login(self.test_admin)
             
        draft_html = bytes.decode(self.client.get(self.draft_url).content)
        self.assertIn('draggable: true,', draft_html)


    def test_style_None(self):
        self.test_collection.icon_style = None
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertRegex(public_html, 'iconContent: "\d+",')
        self.assertIn('preset: "islands#redIcon",', public_html)


    def test_style_default(self):
        self.test_collection.icon_style = 'default'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertRegex(public_html, 'iconContent: "\d+",')
        self.assertIn('preset: "islands#redIcon",', public_html)

        self.test_collection.icon_color = 'blue'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blueIcon",', public_html)

        self.test_collection.icon_circle = True
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blueCircleIcon",', public_html)


    def test_style_stretchy(self):
        self.test_collection.icon_style = 'stretchy'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconContent: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn('preset: "islands#redStretchyIcon",', public_html)

        self.test_collection.icon_color = 'darkOrange'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#darkOrangeStretchyIcon",', public_html)


    def test_style_doted(self):
        self.test_collection.icon_style = 'doted'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#redDotIcon",', public_html)


        self.test_collection.icon_color = 'black'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blackDotIcon",', public_html)
        

        self.test_collection.icon_caption = True
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconCaption: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn('preset: "islands#blackDotIconWithCaption",', public_html)


        self.test_collection.icon_circle = True
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconCaption: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn('preset: "islands#blackCircleDotIconWithCaption",', public_html)


        self.test_collection.icon_caption = False
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blackCircleDotIcon",', public_html)


    def test_style_glif(self):
        self.test_collection.icon_style = 'glif'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#redHomeIcon",', public_html)


        self.test_collection.icon_color = 'violet'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#violetHomeIcon",', public_html)


        self.test_collection.icon_glif = 'Cinema'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#violetCinemaIcon",', public_html)


        self.test_collection.icon_circle = True
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#violetCinemaCircleIcon",', public_html)


    def test_style_image(self):
        self.test_collection.icon_style = 'image'
        self.test_collection.icon_image = 'Test Image'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn("iconLayout: 'default#image',", public_html)


        self.test_collection.icon_caption = True
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconContent: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn("iconLayout: 'default#imageWithContent',", public_html)


    def test_hint(self):
        self.test_collection.hint = 'Hint'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('hintContent: "Hint",', public_html)


    def test_balloon(self):
        self.test_collection.balloon = 'Balloon'
        self.test_collection.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('balloonContent: "Balloon",', public_html)



class ClasterTestCase(TestCase):
    def setUp(self):
        self.test_page = cms.api.create_page('Test Page', 'base.html', 'en')

        test_placeholder = self.test_page.placeholders.get(slot='test')

        test_claster_data = {'title': 'ClasterFormTestCase', 'placemarks': '', 'icon_style': '',
                          'icon_color': 'red', 'icon_circle': False, 'icon_caption': False,
                          'icon_glif': 'Home', 'icon_image': '', 'icon_width': 30, 'icon_height': 30,
                          'icon_offset_horizontal': 0,
                          'icon_offset_vertical': 0, 'icon_content_offset_horizontal': 0,
                          'icon_content_offset_vertical': 0, 'hint': '', 'balloon': '',
                          'disable_click_zoom': True, 'cluster_icon': 'default', 'cluster_color': 'red'}
        self.test_claster = Claster()
        self.test_claster.__dict__.update(test_claster_data)
        self.test_claster.save()

        test_map_data = {'title': 'Test map', 'map_type': 'map', 'lang': 'ru_RU',
                     'auto_placement': True, 'zoom': 11, 'min_zoom': 0, 'max_zoom': 23,
                     'center_lt': 55.76, 'center_lg': 37.64, 'sizing': 'auto', 'width': 320,
                     'height': 180, 'size_update_method': '', 'jq_selector': '', 'jq_event': 'click',
                     'behaviors': (1, 2, 3, 4, 6), 'controls': (5, 6, 7), 'classes': '',
                     'placemarks': '', 'collections': '', 'clasters': '', 'routes': ''}
        test_map = cms.api.add_plugin(test_placeholder, YandexMapsPlugin, 'en')
        test_map.__dict__.update(test_map_data)
        test_map.save()

        test_placemark_data = {'title': 'Test Placemark', 'auto_coordinates': True, 'place': 'Home',
                          'auto_placement': True, 'place_lt': None, 'place_lg': None,
                          'icon_style': 'default', 'icon_color': 'red', 'icon_circle': False,
                          'icon_caption': False, 'icon_glif': 'Home', 'icon_image': '',
                          'icon_width': 30, 'icon_height': 30, 'icon_offset_horizontal': 0,
                          'icon_offset_vertical': 0, 'icon_content_offset_horizontal': 0,
                          'icon_content_offset_vertical': 0, 'hint': '', 'balloon': '',
                          'balloonHeader': '', 'balloonBody': '', 'balloonFooter': '',
                          'point_type': 'wayPoint'}
        self.test_placemark = Placemark()
        self.test_placemark.__dict__.update(test_placemark_data)
        self.test_placemark.save()

        self.test_claster.placemarks.add(self.test_placemark)
        self.test_claster.save()

        test_map.clasters.add(self.test_claster)
        test_map.save()

        self.test_page.publish('en')

        public_test_page = self.test_page.get_public_object()
        public_test_placeholder = public_test_page.placeholders.get(slot='test')

        if CMS_VERSION == "3.4.*":
            self.public_test_map = public_test_placeholder.get_plugins_list()[0].get_bound_plugin()
        else:
            self.public_test_map = public_test_placeholder.get_plugins_list()[0].get_plugin_instance()[0]

        self.draft_url = '{}?edit'.format(self.test_page.get_absolute_url('en'))
        self.public_url = '{}?edit_off'.format(self.test_page.get_absolute_url('en'))

        self.test_admin = User.objects.create_superuser('admin', 'admin@test', 'admin')

        self.client = Client()


    def test_draft_draggable(self):
        if DJANGO_VERSION == "1.8.*":
            self.client.login(username='admin', password='admin')
        else:
            self.client.force_login(self.test_admin)

        draft_html = bytes.decode(self.client.get(self.draft_url).content)
        self.assertIn('draggable: true,', draft_html)

        self.test_placemark.auto_coordinates = False
        self.test_placemark.save()
        if DJANGO_VERSION == "1.8.*":
            self.client.login(username='admin', password='admin')
        else:
            self.client.force_login(self.test_admin)

        draft_html = bytes.decode(self.client.get(self.draft_url).content)
        self.assertIn('draggable: true,', draft_html)


    def test_style_None(self):
        self.test_claster.icon_style = None
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertRegex(public_html, 'iconContent: "\d+",')
        self.assertIn('preset: "islands#redIcon",', public_html)


    def test_style_default(self):
        self.test_claster.icon_style = 'default'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertRegex(public_html, 'iconContent: "\d+",')
        self.assertIn('preset: "islands#redIcon",', public_html)

        self.test_claster.icon_color = 'blue'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blueIcon",', public_html)

        self.test_claster.icon_circle = True
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blueCircleIcon",', public_html)


    def test_style_stretchy(self):
        self.test_claster.icon_style = 'stretchy'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconContent: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn('preset: "islands#redStretchyIcon",', public_html)

        self.test_claster.icon_color = 'darkOrange'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#darkOrangeStretchyIcon",', public_html)


    def test_style_doted(self):
        self.test_claster.icon_style = 'doted'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#redDotIcon",', public_html)


        self.test_claster.icon_color = 'black'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blackDotIcon",', public_html)


        self.test_claster.icon_caption = True
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconCaption: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn('preset: "islands#blackDotIconWithCaption",', public_html)


        self.test_claster.icon_circle = True
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconCaption: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn('preset: "islands#blackCircleDotIconWithCaption",', public_html)


        self.test_claster.icon_caption = False
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#blackCircleDotIcon",', public_html)


    def test_style_glif(self):
        self.test_claster.icon_style = 'glif'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#redHomeIcon",', public_html)


        self.test_claster.icon_color = 'violet'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#violetHomeIcon",', public_html)


        self.test_claster.icon_glif = 'Cinema'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#violetCinemaIcon",', public_html)


        self.test_claster.icon_circle = True
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('preset: "islands#violetCinemaCircleIcon",', public_html)


    def test_style_image(self):
        self.test_claster.icon_style = 'image'
        self.test_claster.icon_image = 'Test Image'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn("iconLayout: 'default#image',", public_html)


        self.test_claster.icon_caption = True
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('iconContent: "{title}",'.format(title=self.test_placemark.title), public_html)
        self.assertIn("iconLayout: 'default#imageWithContent',", public_html)


    def test_hint(self):
        self.test_claster.hint = 'Hint'
        self.test_claster.save()

        self.test_page.publish('en')
 
        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('hintContent: "Hint",', public_html)


    def test_balloon(self):
        self.test_claster.balloon = 'Balloon'
        self.test_claster.save()

        self.test_page.publish('en')

        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('balloonContent: "Balloon",', public_html)



class RouteTestCase(TestCase):
    def setUp(self):
        self.test_page = cms.api.create_page('Test Page', 'base.html', 'en')

        test_placeholder = self.test_page.placeholders.get(slot='test')

        test_route_data = {'title': 'Test Route', 'placemarks': '', 'routing_mode': 'auto',
                          'avoid_traffic_jams': True, 'results': 1, 'route_collor': '#9635ba',
                          'additional_routes_collor': '#7a684e'}
        self.test_route = Route()
        self.test_route.__dict__.update(test_route_data)
        self.test_route.save()

        test_map_data = {'title': 'Test map', 'map_type': 'map', 'lang': 'ru_RU',
                     'auto_placement': True, 'zoom': 11, 'min_zoom': 0, 'max_zoom': 23,
                     'center_lt': 55.76, 'center_lg': 37.64, 'sizing': 'auto', 'width': 320,
                     'height': 180, 'size_update_method': '', 'jq_selector': '', 'jq_event': 'click',
                     'behaviors': (1, 2, 3, 4, 6), 'controls': (5, 6, 7), 'classes': '',
                     'placemarks': '', 'collections': '', 'clasters': '', 'routes': ''}
        test_map = cms.api.add_plugin(test_placeholder, YandexMapsPlugin, 'en')
        test_map.__dict__.update(test_map_data)
        test_map.save()

        test_placemark_data = {'title': 'Test Placemark', 'auto_coordinates': True, 'place': 'Home',
                          'auto_placement': True, 'place_lt': None, 'place_lg': None,
                          'icon_style': 'default', 'icon_color': 'red', 'icon_circle': False,
                          'icon_caption': False, 'icon_glif': 'Home', 'icon_image': '',
                          'icon_width': 30, 'icon_height': 30, 'icon_offset_horizontal': 0,
                          'icon_offset_vertical': 0, 'icon_content_offset_horizontal': 0,
                          'icon_content_offset_vertical': 0, 'hint': '', 'balloon': '',
                          'balloonHeader': '', 'balloonBody': '', 'balloonFooter': '',
                          'point_type': 'wayPoint'}
        self.test_start_placemark = Placemark()
        self.test_start_placemark.__dict__.update(test_placemark_data)
        self.test_start_placemark.save()

        self.test_via_point_placemark = Placemark()
        self.test_via_point_placemark.__dict__.update(test_placemark_data)
        self.test_via_point_placemark.point_type = "viaPoint"
        self.test_via_point_placemark.save()

        self.test_end_placemark = Placemark()
        self.test_end_placemark.__dict__.update(test_placemark_data)
        self.test_end_placemark.auto_coordinates = False
        self.test_end_placemark.place_lg = 31
        self.test_end_placemark.place_lt = 52
        self.test_end_placemark.save()

        self.test_route.placemarks.add(self.test_start_placemark)
        self.test_route.placemarks.add(self.test_via_point_placemark)
        self.test_route.placemarks.add(self.test_end_placemark)
        self.test_route.save()

        test_map.routes.add(self.test_route)
        test_map.save()

        self.test_page.publish('en')

        public_test_page = self.test_page.get_public_object()
        public_test_placeholder = public_test_page.placeholders.get(slot='test')

        if CMS_VERSION == "3.4.*":
            self.public_test_map = public_test_placeholder.get_plugins_list()[0].get_bound_plugin()
        else:
            self.public_test_map = public_test_placeholder.get_plugins_list()[0].get_plugin_instance()[0]

        self.draft_url = '{}?edit'.format(self.test_page.get_absolute_url('en'))
        self.public_url = '{}?edit_off'.format(self.test_page.get_absolute_url('en'))

        self.test_admin = User.objects.create_superuser('admin', 'admin@test', 'admin')

        self.client = Client()


    def test_route(self):
        public_html = bytes.decode(self.client.get(self.public_url).content)
        self.assertIn('yaMap_{map}.geoObjects.add(multiRoute);'.format(map=self.public_test_map.id), public_html)