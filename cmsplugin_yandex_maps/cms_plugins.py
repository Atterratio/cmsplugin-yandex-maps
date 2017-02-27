from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from .admin import PlacemarksInlineAdmin, CollectionsInlineAdmin, ClastersInlineAdmin, RoutesInlineAdmin
from .forms import YandexMapsForm, PlacemarkForm
from .models import YandexMaps



@plugin_pool.register_plugin
class YandexMapsPlugin(CMSPluginBase):
    inlines = (PlacemarksInlineAdmin, CollectionsInlineAdmin, ClastersInlineAdmin, RoutesInlineAdmin)
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
        (_('Advanced'), {'fields': ['lang',
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

        context.update({'collections': instance.collections.all()})

        context.update({'clasters': instance.clasters.all()})

        routes = []
        for route in instance.routes.all():
            placemarks = route.placemarks.through.objects.filter(route=route).order_by('id')
            viaIndexes = []
            for i, place in enumerate(placemarks):
                if place.placemark.point_type == "viaPoint":
                    viaIndexes.append(i)
                    
            routes.append({'placemarks': placemarks, 'viaIndexes': viaIndexes, 'results': route.results,
                           'routing_mode': route.routing_mode, 'route_collor': route.route_collor,
                           'additional_routes_collor': route.additional_routes_collor,
                           'avoid_traffic_jams': route.avoid_traffic_jams},)

        context.update({'routes': routes})

        return context