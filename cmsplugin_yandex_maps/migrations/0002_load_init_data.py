# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command

def load_init_data(apps, schema_editor):
    call_command("loaddata", "cmsplugin_yandex_maps.xml")

class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_yandex_maps', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_init_data),
    ]
