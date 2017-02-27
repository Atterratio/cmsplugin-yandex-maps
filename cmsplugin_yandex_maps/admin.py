from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from .forms import *
from .models import *



class PlacemarksInlineAdmin(admin.StackedInline):
    model = YandexMaps.placemarks.through
    extra = 0



class CollectionsInlineAdmin(admin.StackedInline):
    model = YandexMaps.collections.through
    extra = 0



class PlacemarksCollectionInlineAdmin(admin.StackedInline):
    model = Collection.placemarks.through
    extra = 0



class ClastersInlineAdmin(admin.StackedInline):
    model = YandexMaps.clasters.through
    extra = 0



class PlacemarksClasterInlineAdmin(admin.StackedInline):
    model = Claster.placemarks.through
    extra = 0



class RoutesInlineAdmin(admin.StackedInline):
    model = YandexMaps.routes.through
    extra = 0



class PlacemarksRouteInlineAdmin(admin.StackedInline):
    model = Route.placemarks.through
    extra = 0



@admin.register(Placemark)
class PlacemarkAdmin(admin.ModelAdmin):
    form = PlacemarkForm
    inlines = [PlacemarksInlineAdmin, PlacemarksCollectionInlineAdmin, PlacemarksClasterInlineAdmin,
               PlacemarksRouteInlineAdmin]
    fieldsets = [
        (None, {'fields': ['title', 'auto_coordinates',
                           'place',('place_lt', 'place_lg')]}),
        (_('Text'), {'fields': [('hint', 'balloon')]}),
        (_('Rich text'), {'fields': ['balloonHeader', 'balloonBody', 'balloonFooter'],
                           'classes': ['collapse']}),
        (_('Icon'), {'fields': [('icon_style', 'icon_color', 'icon_glif', 'icon_image'),
                                ('icon_caption', 'icon_circle'),
                                ('icon_width', 'icon_height'),
                                ('icon_offset_horizontal', 'icon_offset_vertical'),
                                ('icon_content_offset_horizontal', 'icon_content_offset_vertical')],
                     'classes': ['collapse']}),
        (_('Advanced'), {'fields': ['point_type',],
                         'classes': ['collapse']}),
    ]


    class Media:
        js = ('https://code.jquery.com/jquery-3.1.1.slim.min.js',
              'cmsplugin_yandex_maps/js/IconStyleAdmin.js',
              'cmsplugin_yandex_maps/js/PlacemarkAdmin.js')



@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    form = CollectionForm
    inlines = (CollectionsInlineAdmin, PlacemarksCollectionInlineAdmin)
    exclude = ['placemarks', ]
    fieldsets = [
        (None, {'fields': ['title',]}),
        (_('Placemarks text'), {'fields': [('hint', 'balloon'),],
                                'classes': ['collapse']}),
        (_('Placemarks icons'), {'fields': [('icon_style', 'icon_color', 'icon_glif', 'icon_image'),
                                ('icon_caption', 'icon_circle'),
                                ('icon_width', 'icon_height'),
                                ('icon_offset_horizontal', 'icon_offset_vertical'),
                                ('icon_content_offset_horizontal', 'icon_content_offset_vertical')],
                     'classes': ['collapse']}),
    ]


    class Media:
        js = ('https://code.jquery.com/jquery-3.1.1.slim.min.js',
              'cmsplugin_yandex_maps/js/IconStyleAdmin.js',
              'cmsplugin_yandex_maps/js/CollectionAdmin.js')



@admin.register(Claster)
class ClasterAdmin(admin.ModelAdmin):
    form = ClasterForm
    inlines = (ClastersInlineAdmin, PlacemarksClasterInlineAdmin)
    exclude = ['placemarks', ]
    fieldsets = [
        (None, {'fields': ['title', 'disable_click_zoom',
                           ('cluster_icon', 'cluster_color')]}),
        (_('Placemarks text'), {'fields': [('hint', 'balloon'),],
                                'classes': ['collapse']}),
        (_('Placemarks icons'), {'fields': [('icon_style', 'icon_color', 'icon_glif', 'icon_image'),
                                ('icon_caption', 'icon_circle'),
                                ('icon_width', 'icon_height'),
                                ('icon_offset_horizontal', 'icon_offset_vertical'),
                                ('icon_content_offset_horizontal', 'icon_content_offset_vertical')],
                     'classes': ['collapse']}),
    ]


    class Media:
        js = ('https://code.jquery.com/jquery-3.1.1.slim.min.js',
              'cmsplugin_yandex_maps/js/IconStyleAdmin.js',
              'cmsplugin_yandex_maps/js/ClasterAdmin.js')



@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    form = RouteForm
    inlines = (RoutesInlineAdmin, PlacemarksRouteInlineAdmin)
    exclude = ['placemarks', ]
    fields = ['title', 'avoid_traffic_jams',
              ('routing_mode', 'results'),
              ('route_collor', 'additional_routes_collor')]


    class Media:
        js = ('https://code.jquery.com/jquery-3.1.1.slim.min.js',
              'cmsplugin_yandex_maps/js/RouteAdmin.js')
        css = { 'all': ('cmsplugin_yandex_maps/css/ColorInput.css',)}