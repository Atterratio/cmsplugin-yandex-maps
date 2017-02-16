# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cmsplugin_yandex_maps.models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_yandex_maps', '0004_from_fk_to_m2m'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=50, blank=True, null=True)),
                ('icon_style', models.CharField(verbose_name='Marker icon style', max_length=8, blank=True, null=True, choices=[('default', 'Default'), ('stretchy', 'Stretchy'), ('doted', 'Doted'), ('glif', 'With glif'), ('image', 'Image')])),
                ('icon_color', models.CharField(verbose_name='Marker icon color', max_length=15, default='red', choices=[('blue', 'Blue'), ('red', 'Red'), ('darkOrange', 'Dark orange'), ('night', 'Night'), ('darkBlue', 'DarkBlue'), ('pink', 'Pink'), ('gray', 'Gray'), ('brown', 'Brown'), ('darkGreen', 'Dark green'), ('violet', 'Violet'), ('black', 'Black'), ('yellow', 'Yellow'), ('green', 'Green'), ('orange', 'Orange'), ('lightBlue', 'Light blue'), ('olive', 'Olive')])),
                ('icon_circle', models.BooleanField(verbose_name='Circle icon', default=False)),
                ('icon_caption', models.BooleanField(verbose_name='Caption', default=False)),
                ('icon_glif', models.CharField(verbose_name='Icon glif', max_length=30, default='Home', choices=[('Home', 'Home'), ('Airport', 'Airport'), ('Bar', 'Bar'), ('Food', 'Food'), ('Cinema', 'Cinema'), ('MassTransit', 'Mass Transit'), ('Toilet', 'Toilet'), ('Beach', 'Beach'), ('Zoo', 'Zoo'), ('Underpass', 'Underpass'), ('Run', 'Run'), ('Bicycle', 'Bicycle'), ('Bicycle2', 'Bicycle2'), ('Garden', 'Garden'), ('Observation', 'Observation'), ('Entertainment', 'Entertainment'), ('Family', 'Family'), ('Theater', 'Theater'), ('Book', 'Book'), ('Waterway', 'Waterway'), ('RepairShop', 'Repair Shop'), ('Post', 'Post'), ('WaterPark', 'Water Park'), ('Worship', 'Worship'), ('Fashion', 'Fashion'), ('Waste', 'Waste'), ('Money', 'Money'), ('Hydro', 'Hydro'), ('Science', 'Science'), ('Auto', 'Auto'), ('Shopping', 'Shopping'), ('Sport', 'Sport'), ('Video', 'Video'), ('Railway', 'Railway'), ('Park', 'Park'), ('Pocket', 'Pocket'), ('NightClub', 'Night Club'), ('Pool', 'Pool'), ('Medical', 'Medical'), ('Vegetation', 'Vegetation'), ('Government', 'Government'), ('Circus', 'Circus'), ('RapidTransit', 'Rapid Transit'), ('Education', 'Education'), ('Mountain', 'Mountain'), ('CarWash', 'Car Wash'), ('Factory', 'Factory'), ('Court', 'Court'), ('Hotel', 'Hotel'), ('Christian', 'Christian'), ('Laundry', 'Laundry'), ('Souvenirs', 'Souvenirs'), ('Dog', 'Dog'), ('Leisure', 'Leisure')])),
                ('icon_image', models.ImageField(verbose_name='Icon image', max_length=500, blank=True, null=True, upload_to=cmsplugin_yandex_maps.models.upload_path_handler)),
                ('icon_width', models.IntegerField(verbose_name='Icon width', default=30)),
                ('icon_height', models.IntegerField(verbose_name='Icon height', default=30)),
                ('icon_offset_horizontal', models.IntegerField(verbose_name='Icon offset horizontal', default=0)),
                ('icon_offset_vertical', models.IntegerField(verbose_name='Icon offset vertical', default=0)),
                ('icon_content_offset_horizontal', models.IntegerField(verbose_name='Icon content offset horizontal', default=0)),
                ('icon_content_offset_vertical', models.IntegerField(verbose_name='Icon content offset vertical', default=0)),
                ('hint', models.CharField(verbose_name='Placemark hint', max_length=140, blank=True, null=True)),
                ('balloon', models.CharField(verbose_name='Balloon content', max_length=300, blank=True, null=True)),
                ('disable_click_zoom', models.BooleanField(verbose_name='Disable click zoom', default=True)),
                ('cluster_icon', models.CharField(verbose_name='Cluster icon', max_length=8, default='default', choices=[('default', 'Default'), ('inverted', 'Inverted')])),
                ('cluster_color', models.CharField(verbose_name='Cluster icon color', max_length=15, default='red', choices=[('blue', 'Blue'), ('red', 'Red'), ('darkOrange', 'Dark orange'), ('night', 'Night'), ('darkBlue', 'DarkBlue'), ('pink', 'Pink'), ('gray', 'Gray'), ('brown', 'Brown'), ('darkGreen', 'Dark green'), ('violet', 'Violet'), ('black', 'Black'), ('yellow', 'Yellow'), ('green', 'Green'), ('orange', 'Orange'), ('lightBlue', 'Light blue'), ('olive', 'Olive')])),
            ],
            options={
                'verbose_name': 'Claster',
                'verbose_name_plural': 'Clasters',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=50, blank=True, null=True)),
                ('icon_style', models.CharField(verbose_name='Marker icon style', max_length=8, blank=True, null=True, choices=[('default', 'Default'), ('stretchy', 'Stretchy'), ('doted', 'Doted'), ('glif', 'With glif'), ('image', 'Image')])),
                ('icon_color', models.CharField(verbose_name='Marker icon color', max_length=15, default='red', choices=[('blue', 'Blue'), ('red', 'Red'), ('darkOrange', 'Dark orange'), ('night', 'Night'), ('darkBlue', 'DarkBlue'), ('pink', 'Pink'), ('gray', 'Gray'), ('brown', 'Brown'), ('darkGreen', 'Dark green'), ('violet', 'Violet'), ('black', 'Black'), ('yellow', 'Yellow'), ('green', 'Green'), ('orange', 'Orange'), ('lightBlue', 'Light blue'), ('olive', 'Olive')])),
                ('icon_circle', models.BooleanField(verbose_name='Circle icon', default=False)),
                ('icon_caption', models.BooleanField(verbose_name='Caption', default=False)),
                ('icon_glif', models.CharField(verbose_name='Icon glif', max_length=30, default='Home', choices=[('Home', 'Home'), ('Airport', 'Airport'), ('Bar', 'Bar'), ('Food', 'Food'), ('Cinema', 'Cinema'), ('MassTransit', 'Mass Transit'), ('Toilet', 'Toilet'), ('Beach', 'Beach'), ('Zoo', 'Zoo'), ('Underpass', 'Underpass'), ('Run', 'Run'), ('Bicycle', 'Bicycle'), ('Bicycle2', 'Bicycle2'), ('Garden', 'Garden'), ('Observation', 'Observation'), ('Entertainment', 'Entertainment'), ('Family', 'Family'), ('Theater', 'Theater'), ('Book', 'Book'), ('Waterway', 'Waterway'), ('RepairShop', 'Repair Shop'), ('Post', 'Post'), ('WaterPark', 'Water Park'), ('Worship', 'Worship'), ('Fashion', 'Fashion'), ('Waste', 'Waste'), ('Money', 'Money'), ('Hydro', 'Hydro'), ('Science', 'Science'), ('Auto', 'Auto'), ('Shopping', 'Shopping'), ('Sport', 'Sport'), ('Video', 'Video'), ('Railway', 'Railway'), ('Park', 'Park'), ('Pocket', 'Pocket'), ('NightClub', 'Night Club'), ('Pool', 'Pool'), ('Medical', 'Medical'), ('Vegetation', 'Vegetation'), ('Government', 'Government'), ('Circus', 'Circus'), ('RapidTransit', 'Rapid Transit'), ('Education', 'Education'), ('Mountain', 'Mountain'), ('CarWash', 'Car Wash'), ('Factory', 'Factory'), ('Court', 'Court'), ('Hotel', 'Hotel'), ('Christian', 'Christian'), ('Laundry', 'Laundry'), ('Souvenirs', 'Souvenirs'), ('Dog', 'Dog'), ('Leisure', 'Leisure')])),
                ('icon_image', models.ImageField(verbose_name='Icon image', max_length=500, blank=True, null=True, upload_to=cmsplugin_yandex_maps.models.upload_path_handler)),
                ('icon_width', models.IntegerField(verbose_name='Icon width', default=30)),
                ('icon_height', models.IntegerField(verbose_name='Icon height', default=30)),
                ('icon_offset_horizontal', models.IntegerField(verbose_name='Icon offset horizontal', default=0)),
                ('icon_offset_vertical', models.IntegerField(verbose_name='Icon offset vertical', default=0)),
                ('icon_content_offset_horizontal', models.IntegerField(verbose_name='Icon content offset horizontal', default=0)),
                ('icon_content_offset_vertical', models.IntegerField(verbose_name='Icon content offset vertical', default=0)),
                ('hint', models.CharField(verbose_name='Placemark hint', max_length=140, blank=True, null=True)),
                ('balloon', models.CharField(verbose_name='Balloon content', max_length=300, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=50, blank=True, null=True)),
                ('routing_mode', models.CharField(verbose_name='Routing mode', max_length=11, default='auto', choices=[('auto', 'Auto'), ('masstransit', 'Mass Transit'), ('pedestrian', 'Pedestrian')])),
                ('avoid_traffic_jams', models.BooleanField(verbose_name='Avoid traffic jams', default=False)),
                ('results', models.IntegerField(verbose_name='Results', default=1)),
                ('route_collor', models.CharField(verbose_name='Route collor', max_length=7, default='#9635ba')),
                ('additional_routes_collor', models.CharField(verbose_name='Route collor', max_length=7, default='#7a684e')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
        migrations.RemoveField(
            model_name='yandexmaps',
            name='cluster_color',
        ),
        migrations.RemoveField(
            model_name='yandexmaps',
            name='cluster_disable_click_zoom',
        ),
        migrations.RemoveField(
            model_name='yandexmaps',
            name='cluster_icon',
        ),
        migrations.RemoveField(
            model_name='yandexmaps',
            name='clusterisation',
        ),
        migrations.RemoveField(
            model_name='yandexmaps',
            name='route',
        ),
        migrations.AddField(
            model_name='placemark',
            name='point_type',
            field=models.CharField(verbose_name='Point type', max_length=8, default='wayPoint', choices=[('wayPoint', 'Way point'), ('viaPoint', 'Transit point')], help_text='Used only in route'),
        ),
        migrations.AlterField(
            model_name='yandexmaps',
            name='behaviors',
            field=models.ManyToManyField(verbose_name='Behaviors', blank=True, default=(1, 2, 3, 4, 6), help_text="Sorry for the Russian, I'm too lazy and just copied the description from the documentation", to='cmsplugin_yandex_maps.Behavior'),
        ),
        migrations.AlterField(
            model_name='yandexmaps',
            name='controls',
            field=models.ManyToManyField(verbose_name='Controls', blank=True, default=(5, 6, 7), help_text="Sorry for the Russian, I'm too lazy and just copied the description from the documentation", to='cmsplugin_yandex_maps.Control'),
        ),
        migrations.AddField(
            model_name='route',
            name='placemarks',
            field=models.ManyToManyField(verbose_name='Placemark', blank=True, to='cmsplugin_yandex_maps.Placemark'),
        ),
        migrations.AddField(
            model_name='collection',
            name='placemarks',
            field=models.ManyToManyField(verbose_name='Placemark', blank=True, to='cmsplugin_yandex_maps.Placemark'),
        ),
        migrations.AddField(
            model_name='claster',
            name='placemarks',
            field=models.ManyToManyField(verbose_name='Placemark', blank=True, to='cmsplugin_yandex_maps.Placemark'),
        ),
        migrations.AddField(
            model_name='yandexmaps',
            name='clasters',
            field=models.ManyToManyField(verbose_name='Claster', blank=True, to='cmsplugin_yandex_maps.Claster'),
        ),
        migrations.AddField(
            model_name='yandexmaps',
            name='collections',
            field=models.ManyToManyField(verbose_name='Collection', blank=True, to='cmsplugin_yandex_maps.Collection'),
        ),
        migrations.AddField(
            model_name='yandexmaps',
            name='routes',
            field=models.ManyToManyField(verbose_name='Route', blank=True, to='cmsplugin_yandex_maps.Route'),
        ),
    ]
