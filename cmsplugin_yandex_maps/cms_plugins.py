from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import ungettext_lazy
from django.utils.translation import ugettext_lazy as _

from .forms import YandexMapsForm, PlacemarkForm
from .models import YandexMaps
from .admin import PlacemarksInlineAdmin, CollectionsInlineAdmin, ClastersInlineAdmin



@plugin_pool.register_plugin
class YandexMapsPlugin(CMSPluginBase):
    inlines = (PlacemarksInlineAdmin, CollectionsInlineAdmin, ClastersInlineAdmin)
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