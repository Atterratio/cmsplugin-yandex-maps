from django.test import TestCase
from django.test import Client
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser, User
import cms.api
from cms import page_rendering
import os

from cmsplugin_yandex_maps.cms_plugins import YandexMapsPlugin
from cmsplugin_yandex_maps.models import YandexMaps

try:
    CMS_VERSION = os.environ['CMS_VERSION']
except:
    CMS_VERSION = "3.4.*"

class YandexMapsPluginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_empty_map(self):
        test_page = cms.api.create_page('Test Page', 'base.html', 'en')
        test_placeholder = test_page.placeholders.get(slot='test')
        cms.api.add_plugin(test_placeholder, YandexMapsPlugin, 'en')
        test_page.publish('en')
        public_test_page = test_page.get_public_object()
        public_test_placeholder = public_test_page.placeholders.get(slot='test')
        if CMS_VERSION == "3.4.*":
            public_test_plugin = public_test_placeholder.get_plugins_list()[0].get_bound_plugin()
        else:
            public_test_plugin = public_test_placeholder.get_plugins_list()[0].get_plugin_instance()[0]
        public_url = test_page.get_public_url()
        public_html = bytes.decode(self.client.get(public_url).content)
        self.assertInHTML('<div class="cmsplugin-ya-maps ">\n    <div id="map-{}" style="width: 100%; height: 100%;"></div>\n</div>'.format(public_test_plugin.id), public_html)