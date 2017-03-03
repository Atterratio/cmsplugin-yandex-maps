import django
from django.conf import settings
import os, sys
gettext = lambda s: s

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
sys.path.append(BASE_DIR)
os.chdir(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmsplugin_yandex_maps.tests.settings")

django.setup()
from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)
  
failures = test_runner.run_tests(['cmsplugin_yandex_maps'])
if failures:
    sys.exit(failures)