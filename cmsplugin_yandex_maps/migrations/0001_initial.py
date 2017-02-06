# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cmsplugin_yandex_maps.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Behavior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('behavior', models.CharField(verbose_name='Behavior', max_length=30, unique=True)),
                ('description', models.CharField(verbose_name='Description', max_length=300, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('control', models.CharField(verbose_name='Control', max_length=30, unique=True)),
                ('description', models.CharField(verbose_name='Description', max_length=300, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Placemark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=50, blank=True, null=True)),
                ('auto_coordinates', models.BooleanField(verbose_name='Auto coordinates', default=True)),
                ('place', models.CharField(verbose_name='Place', max_length=300, blank=True, null=True)),
                ('place_lt', models.FloatField(verbose_name='Latitude', blank=True, null=True)),
                ('place_lg', models.FloatField(verbose_name='Longitude', blank=True, null=True)),
                ('icon_color', models.CharField(verbose_name='Marker icon color', max_length=15, default='red', choices=[('blue', 'Blue'), ('red', 'Red'), ('darkOrange', 'Dark orange'), ('night', 'Night'), ('darkBlue', 'DarkBlue'), ('pink', 'Pink'), ('gray', 'Gray'), ('brown', 'Brown'), ('darkGreen', 'Dark green'), ('violet', 'Violet'), ('black', 'Black'), ('yellow', 'Yellow'), ('green', 'Green'), ('orange', 'Orange'), ('lightBlue', 'Light blue'), ('olive', 'Olive')])),
                ('icon_style', models.CharField(verbose_name='Marker icon style', max_length=8, default='default', choices=[('default', 'Default'), ('stretchy', 'Stretchy'), ('doted', 'Doted'), ('glif', 'With glif'), ('image', 'Image')])),
                ('icon_circle', models.BooleanField(verbose_name='Circle icon', default=False)),
                ('icon_caption', models.BooleanField(verbose_name='Caption', default=False)),
                ('icon_glif', models.CharField(verbose_name='Icon glif', max_length=30, default='Home', choices=[('Home', 'Home'), ('Airport', 'Airport'), ('Bar', 'Bar'), ('Food', 'Food'), ('Cinema', 'Cinema'), ('MassTransit', 'Mass Transit'), ('Toile', 'Toile'), ('Beach', 'Beach'), ('Zoo', 'Zoo'), ('Underpass', 'Underpass'), ('Run', 'Run'), ('Bicycle', 'Bicycle'), ('Bicycle2', 'Bicycle2'), ('Garden', 'Garden'), ('Observation', 'Observation'), ('Entertainment', 'Entertainment'), ('Family', 'Family'), ('Theater', 'Theater'), ('Book', 'Book'), ('Waterway', 'Waterway'), ('RepairShop', 'Repair Shop'), ('Post', 'Post'), ('WaterPark', 'Water Park'), ('Worship', 'Worship'), ('Fashion', 'Fashion'), ('Waste', 'Waste'), ('Money', 'Money'), ('Hydro', 'Hydro'), ('Science', 'Science'), ('Auto', 'Auto'), ('Shopping', 'Shopping'), ('Sport', 'Sport'), ('Video', 'Video'), ('Railway', 'Railway'), ('Park', 'Park'), ('Pocket', 'Pocket'), ('NightClub', 'Night Club'), ('Pool', 'Pool'), ('Medical', 'Medical'), ('Vegetation', 'Vegetation'), ('Government', 'Government'), ('Circus', 'Circus'), ('RapidTransit', 'Rapid Transit'), ('Education', 'Education'), ('Mountain', 'Mountain'), ('CarWash', 'Car Wash'), ('Factory', 'Factory'), ('Court', 'Court'), ('Hotel', 'Hotel'), ('Christian', 'Christian'), ('Laundry', 'Laundry'), ('Souvenirs', 'Souvenirs'), ('Dog', 'Dog'), ('Leisure', 'Leisure')])),
                ('icon_image', models.ImageField(verbose_name='Icon image', max_length=500, blank=True, null=True, upload_to=cmsplugin_yandex_maps.models.upload_path_handler)),
                ('icon_width', models.IntegerField(verbose_name='Icon width', default=30)),
                ('icon_height', models.IntegerField(verbose_name='Icon height', default=30)),
                ('icon_offset_horizontal', models.IntegerField(verbose_name='Icon offset horizontal', default=0)),
                ('icon_offset_vertical', models.IntegerField(verbose_name='Icon offset vertical', default=0)),
                ('icon_content_offset_horizontal', models.IntegerField(verbose_name='Icon content offset horizontal', default=0)),
                ('icon_content_offset_vertical', models.IntegerField(verbose_name='Icon content offset vertical', default=0)),
                ('hint', models.CharField(verbose_name='Placemark hint', max_length=140, blank=True, null=True)),
                ('balloon', models.CharField(verbose_name='Balloon content', max_length=300, blank=True, null=True)),
                ('balloonHeader', models.TextField(verbose_name='Balloon header', blank=True, help_text='Can use some html, please be careful!')),
                ('balloonBody', models.TextField(verbose_name='Balloon body', blank=True, help_text='Replace "Balloon content".                                     Can use some html, please be careful!')),
                ('balloonFooter', models.TextField(verbose_name='Balloon footer', blank=True, help_text='Can use some html, please be careful!')),
            ],
        ),
        migrations.CreateModel(
            name='YandexMaps',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='cmsplugin_yandex_maps_yandexmaps', parent_link=True, to='cms.CMSPlugin')),
                ('title', models.CharField(verbose_name='Map title', max_length=140, blank=True, null=True)),
                ('map_type', models.CharField(verbose_name='Initial type', max_length=10, default='map', choices=[('map', 'Scheme'), ('satellite', 'Satellite'), ('hybrid', 'Hybryd')])),
                ('route', models.BooleanField(verbose_name='Create route', default=False, help_text='Create route between points (unstable)')),
                ('clusterisation', models.BooleanField(verbose_name='Clusterisation', default=True)),
                ('cluster_disable_click_zoom', models.BooleanField(verbose_name='Disable click zoom', default=True)),
                ('cluster_icon', models.CharField(verbose_name='Cluster icon', max_length=8, default='default', choices=[('default', 'Default'), ('inverted', 'Inverted')])),
                ('cluster_color', models.CharField(verbose_name='Cluster icon color', max_length=15, default='red', choices=[('blue', 'Blue'), ('red', 'Red'), ('darkOrange', 'Dark orange'), ('night', 'Night'), ('darkBlue', 'DarkBlue'), ('pink', 'Pink'), ('gray', 'Gray'), ('brown', 'Brown'), ('darkGreen', 'Dark green'), ('violet', 'Violet'), ('black', 'Black'), ('yellow', 'Yellow'), ('green', 'Green'), ('orange', 'Orange'), ('lightBlue', 'Light blue'), ('olive', 'Olive')])),
                ('lang', models.CharField(verbose_name='Language', max_length=5, default='ru_RU', choices=[('ru_RU', 'Русский'), ('en_RU', 'English'), ('uk_UA', 'Українська'), ('tr_TR', 'Türk')])),
                ('auto_placement', models.BooleanField(verbose_name='Auto placement', default=True)),
                ('zoom', models.IntegerField(verbose_name='Zoom', default=12)),
                ('min_zoom', models.IntegerField(verbose_name='Minimum zoom', default=0)),
                ('max_zoom', models.IntegerField(verbose_name='Maximum zoom', default=23)),
                ('center_lt', models.FloatField(verbose_name='Latitude', default=55.76)),
                ('center_lg', models.FloatField(verbose_name='Longitude', default=37.64)),
                ('auto_size', models.BooleanField(verbose_name='Auto size', default=True, help_text='If checked, the map will try to take all                                     available width, keeping aspect ratio')),
                ('width', models.IntegerField(verbose_name='Width')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('classes', models.TextField(verbose_name='CSS classes', blank=True)),
                ('behaviors', models.ManyToManyField(verbose_name='Behaviors', default=(1, 2, 3, 4, 6), help_text="Sorry for the Russian, I'm too lazy and just                                     copied the description from the documentation", to='cmsplugin_yandex_maps.Behavior')),
                ('controls', models.ManyToManyField(verbose_name='Controls', default=(5, 6, 7), help_text="Sorry for the Russian, I'm too lazy and just                                     copied the description from the documentation", to='cmsplugin_yandex_maps.Control')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='placemark',
            name='map',
            field=models.ForeignKey(to='cmsplugin_yandex_maps.YandexMaps'),
        ),
    ]
