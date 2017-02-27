from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _



class YandexMapsApphook(CMSApp):
    app_name = "yamaps"
    name = _("Yandex Maps")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["cmsplugin_yandex_maps.urls"]

apphook_pool.register(YandexMapsApphook)