from aldryn_client import forms

class Form(forms.BaseForm):
    enable_drag_and_drop = forms.CheckboxField(
        'Enable ajax drag and drop Placemark and Map in draft',
        required=False)

    def to_settings(self, data, settings):
        if data['enable_drag_and_drop']:
            settings['ADDON_URLS'].append('cmsplugin_yandex_maps.addon_urls')

        return settings