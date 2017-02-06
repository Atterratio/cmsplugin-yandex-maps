from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import YandexMapModel, Placemark


class YandexMapForm(forms.ModelForm):
    zoom = forms.IntegerField(label=_('Zoom'), initial=12, min_value=0, max_value=23)
    min_zoom = forms.IntegerField(label=_('Minimum zoom'), initial=0, min_value=0, max_value=23)
    max_zoom = forms.IntegerField(label=_('Maximum zoom'), initial=23, min_value=0, max_value=23)
 
    width = forms.IntegerField(label=_('Width'), min_value=1)
    height = forms.IntegerField(label=_('Height'), min_value=1)
 
    center_lt = forms.DecimalField(label=_('Latitude'), initial=55.76, min_value=-90, max_value=90, decimal_places=7)
    center_lg = forms.DecimalField(label=_('Longitude'), initial=37.64, min_value=-180, max_value=180, decimal_places=7)
 
    class Meta:
        model = YandexMapModel
        fields = '__all__'



class PlacemarkForm(forms.ModelForm):
    place_lt = forms.DecimalField(label=_('Latitude'), required=False, min_value=-90,
                                  max_value=90, decimal_places=7)
    place_lg = forms.DecimalField(label=_('Longitude'), required=False, min_value=-180,
                                  max_value=180, decimal_places=7)
    icon_width = forms.IntegerField(label=_('Icon width'), initial=30, min_value=1)
    icon_height = forms.IntegerField(label=_('Icon height'), initial=30, min_value=1)
    icon_offset_horizontal = forms.IntegerField(label=_('Icon offset horizontal'), initial=0, min_value=0)
    icon_offset_vertical = forms.IntegerField(label=_('Icon offset vertical'), initial=0, min_value=0)
    icon_content_offset_horizontal = forms.IntegerField(label=_('Icon content offset horizontal'), initial=0, min_value=0)
    icon_content_offset_vertical = forms.IntegerField(label=_('Icon content offset vertical'), initial=0, min_value=0)


    def clean(self):
        cleaned_data = super(PlacemarkForm, self).clean()

        auto_coordinates = cleaned_data['auto_coordinates']
        place = cleaned_data['place']
        place_lt = cleaned_data['place_lt']
        place_lg = cleaned_data['place_lg']

        if auto_coordinates:
            if not place:
                self.add_error('place', _('This field requered if «Auto Coordinates» enable'))
        else:
            if place_lt is None:
                self.add_error('place_lt', _('This field requered if «Auto Coordinates» disable'))
            if place_lg is None:
                self.add_error('place_lg', _('This field requered if «Auto Coordinates» disable'))

        icon_style = cleaned_data['icon_style']
        icon_image = cleaned_data['icon_image']
        if icon_style == "image" and not icon_image:
            self.add_error('icon_image', _('Image required'))

        return cleaned_data

    class Meta:
        model = Placemark
        fields = '__all__'
