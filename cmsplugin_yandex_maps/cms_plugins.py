from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import ugettext as _

from .forms import YandexMapsForm, PlacemarkForm
from .models import YandexMaps, Behavior, Control, Placemark



class PlacemarkAdmin(admin.StackedInline):
    model = Placemark
    extra = 0
    form = PlacemarkForm
    fieldsets = [
        (None, {'fields': ['map', 'title', 'auto_coordinates',
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


admin.site.register(Behavior)
admin.site.register(Control)



class YandexMapsPlugin(CMSPluginBase):
    model = YandexMaps
    name = _("Yandex Maps Plugin")
    render_template = "cmsplugin_yandex_maps/yandex_maps.djhtml"
    fieldsets = [
        (None, {'fields': ['route', 'title', 'map_type']}),
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
        (_('Advanced'), {'fields': ['lang',
                                    'behaviors',
                                    'controls',
                                    ('min_zoom', 'max_zoom'),
                                    'classes'],
                         'classes': ['collapse']}),
    ]
    inlines = (PlacemarkAdmin, )
    form = YandexMapsForm
    class Media:
        js = ('cmsplugin_yandex_maps/js/admin.js',)


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

        context.update({'placemarks': instance.placemark_set.all()})

        return context


plugin_pool.register_plugin(YandexMapsPlugin)