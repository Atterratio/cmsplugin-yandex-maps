import json

from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import YandexMaps, Placemark


@require_POST
def update_placement(request):
    if request.user.has_perm('cms.change_page') and request.user.has_perm('cmsplugin_yandex_maps.change_yandexmaps'):
        data = json.loads(bytes.decode(request.body))
        map = YandexMaps.objects.get(pk=data['id'])
        map.auto_placement = False
        map.zoom = data['zoom']
        map.center_lt = data['center'][0]
        map.center_lg = data['center'][1]
        map.save()
        return JsonResponse({'status': 'ok'})
    else:
        return HttpResponseForbidden()


@require_POST
def update_placemark(request):
    if request.user.has_perm('cms.change_page') and request.user.has_perm('cmsplugin_yandex_maps.change_placemark'):
        data = json.loads(bytes.decode(request.body))
        placemark = Placemark.objects.get(pk=data['id'])
        placemark.auto_coordinates = False
        placemark.place_lt = data['position'][0]
        placemark.place_lg = data['position'][1]
        placemark.save()
        return JsonResponse({'status': 'ok'})
    else:
        return HttpResponseForbidden()