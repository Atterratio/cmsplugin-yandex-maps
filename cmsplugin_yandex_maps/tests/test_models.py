from django.test import TestCase
from cmsplugin_yandex_maps.models import *



# Create your tests here.
class PreloadDataTestCase(TestCase):
    def test_behaviors(self):
        self.assertIsNotNone(Behavior.objects.get(behavior="drag"))
        self.assertIsNotNone(Behavior.objects.get(behavior="dblClickZoom"))
        self.assertIsNotNone(Behavior.objects.get(behavior="multiTouch"))
        self.assertIsNotNone(Behavior.objects.get(behavior="scrollZoom"))
        self.assertIsNotNone(Behavior.objects.get(behavior="leftMouseButtonMagnifier"))
        self.assertIsNotNone(Behavior.objects.get(behavior="rightMouseButtonMagnifier"))
        self.assertIsNotNone(Behavior.objects.get(behavior="ruler"))
        self.assertIsNotNone(Behavior.objects.get(behavior="routeEditor"))


    def test_controls(self):
        self.assertIsNotNone(Control.objects.get(control="geolocationControl"))
        self.assertIsNotNone(Control.objects.get(control="searchControl"))
        self.assertIsNotNone(Control.objects.get(control="routeEditor"))
        self.assertIsNotNone(Control.objects.get(control="trafficControl"))
        self.assertIsNotNone(Control.objects.get(control="typeSelector"))
        self.assertIsNotNone(Control.objects.get(control="fullscreenControl"))
        self.assertIsNotNone(Control.objects.get(control="zoomControl"))
        self.assertIsNotNone(Control.objects.get(control="rulerControl"))