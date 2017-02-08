from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import ungettext_lazy
from django.utils.translation import ugettext_lazy as _

from .forms import YandexMapsForm, PlacemarkForm
from .models import YandexMaps, Behavior, Control, Placemark


class PlacemarksInlineAdmin(admin.StackedInline):
    model = YandexMaps.placemarks.through
    extra = 0
    
    verbose_name = ungettext_lazy("Placemark", "Placemarks", 1)
    verbose_name_plural = ungettext_lazy("Placemark", "Placemarks", 2)



@admin.register(Placemark)
class PlacemarkAdmin(admin.ModelAdmin):
    form = PlacemarkForm
    inlines = [PlacemarksInlineAdmin, ]
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
                     'classes': ['collapse']})
    ]


    class Media:
        js = ('https://code.jquery.com/jquery-3.1.1.slim.min.js',
              'cmsplugin_yandex_maps/js/PlacemarkAdmin.js')



admin.site.register(Behavior)
admin.site.register(Control)



@plugin_pool.register_plugin
class YandexMapsPlugin(CMSPluginBase):
    inlines = (PlacemarksInlineAdmin, )
    form = YandexMapsForm
    model = YandexMaps
    name = _("Yandex Maps Plugin")
    render_template = "cmsplugin_yandex_maps/yandex_maps.djhtml"
    fieldsets = [
        (None, {'fields': ['title', 'map_type']}),
        (_('Sizing'), {'fields': ['sizing', 
                                  ('width', 'height'),
                                  'size_update_method',
                                  ('jq_selector', 'jq_event')],
                               'classes': ['collapse']}),
        (_('Clusterisation'), {'fields': [('clusterisation', 'cluster_disable_click_zoom'),
                                          ('cluster_icon', 'cluster_color')],
                               'classes': ['collapse']}),
        (_('Placement'), {'fields':['auto_placement',
                                    'zoom',
                                    ('center_lt', 'center_lg')],
                          'classes': ['collapse']}),
        (_('Advanced'), {'fields': ['route',
                                    'lang',
                                    'behaviors',
                                    'controls',
                                    ('min_zoom', 'max_zoom'),
                                    'classes'],
                         'classes': ['collapse']}),
    ]
    exclude = ['placemarks', ]
    verbose_name = _("Yandex Maps")
    verbose_name_plural = _("Yandex Maps")

    class Media:
        js = ('cmsplugin_yandex_maps/js/YandexMapsAdmin.js',)


    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        behaviors = []
        for behavior in instance.behaviors.all():
            behaviors.append(behavior.behavior)
        context.update({'behaviors': behaviors})

        controls = []
        for control in instance.controls.all():
            controls.append(control.control)
        context.update({'controls': controls})

        context.update({'placemarks': instance.placemarks.all()})

        return context