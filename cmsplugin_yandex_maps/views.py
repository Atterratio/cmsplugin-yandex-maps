from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
import json
from .models import YandexMaps

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