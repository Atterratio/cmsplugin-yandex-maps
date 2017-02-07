from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import YandexMaps, Placemark


class YandexMapsForm(forms.ModelForm):
    zoom = forms.IntegerField(label=_('Zoom'), initial=12, min_value=0, max_value=23)
    min_zoom = forms.IntegerField(label=_('Minimum zoom'), initial=0, min_value=0, max_value=23)
    max_zoom = forms.IntegerField(label=_('Maximum zoom'), initial=23, min_value=0, max_value=23)

    center_lt = forms.DecimalField(label=_('Latitude'), initial=55.76, min_value=-90, max_value=90, decimal_places=7)
    center_lg = forms.DecimalField(label=_('Longitude'), initial=37.64, min_value=-180, max_value=180, decimal_places=7)

    width = forms.IntegerField(label=_('Width'), initial=320, min_value=1)
    height = forms.IntegerField(label=_('Height'), initial=180, min_value=1)
    jq_selector = forms.CharField(label=_('jQuery selector'), required=False)


    def clean_jq_selector(self):
        jq_selector = self.cleaned_data['jq_selector']
        
        return jq_selector.replace('"', "'").strip("'")


    def clean(self):
        cleaned_data = super(YandexMapsForm, self).clean()
        size_update_method = cleaned_data['size_update_method']
        jq_selector = cleaned_data['jq_selector']
        jq_event = cleaned_data['jq_event']
        
        if size_update_method:
            if not jq_selector:
                self.add_error('jq_selector', forms.ValidationError(forms.fields.Field.default_error_messages['required']))

        if size_update_method == 'jq_event':
            if not jq_event:
                self.add_error('jq_event', forms.ValidationError(forms.fields.Field.default_error_messages['required']))

    class Meta:
        model = YandexMaps
        fields = '__all__'



class PlacemarkForm(forms.ModelForm):
    place_lt = forms.DecimalField(label=_('Latitude'), required=False, min_value=-90,
                                  max_value=90, decimal_places=14)
    place_lg = forms.DecimalField(label=_('Longitude'), required=False, min_value=-180,
                                  max_value=180, decimal_places=14)

    icon_width = forms.IntegerField(label=_('Icon width'), initial=30, min_value=1)
    icon_height = forms.IntegerField(label=_('Icon height'), initial=30, min_value=1)
    icon_offset_horizontal = forms.IntegerField(label=_('Icon offset horizontal'), initial=0, min_value=0)
    icon_offset_vertical = forms.IntegerField(label=_('Icon offset vertical'), initial=0, min_value=0)
    icon_content_offset_horizontal = forms.IntegerField(label=_('Icon content offset horizontal'), initial=0, min_value=0)
    icon_content_offset_vertical = forms.IntegerField(label=_('Icon content offset vertical'), initial=0, min_value=0)

    balloonHeader = forms.CharField(label=_('Balloon header'), widget=forms.Textarea, required=False,
                                    help_text = _("Can use some html, please be careful!"))
    balloonBody = forms.CharField(label=_('Balloon body'), widget=forms.Textarea, required=False,
                                    help_text = _('Replace "Balloon content". Can use some html, please be careful!'))
    balloonFooter = forms.CharField(label=_('Balloon footer'), widget=forms.Textarea, required=False,
                                    help_text = _("Can use some html, please be careful!"))


    def clean_balloonBody(self):
        balloonBody = self.cleaned_data['balloonBody']
        
        return balloonBody.replace('"', "'")
        
    def clean(self):
        cleaned_data = super(PlacemarkForm, self).clean()

        auto_coordinates = cleaned_data['auto_coordinates']
        place = cleaned_data['place']
        place_lt = cleaned_data['place_lt']
        place_lg = cleaned_data['place_lg']

        if auto_coordinates:
            if not place:
                self.add_error('place', forms.ValidationError(forms.fields.Field.default_error_messages['required']))
        else:
            if not place_lt:
                self.add_error('place_lt', forms.ValidationError(forms.fields.Field.default_error_messages['required']))
            if not place_lg:
                self.add_error('place_lg', forms.ValidationError(forms.fields.Field.default_error_messages['required']))

        icon_style = cleaned_data['icon_style']
        icon_image = cleaned_data['icon_image']
        if icon_style == "image" and not icon_image:
            self.add_error('icon_image', _('Image required'))

        return cleaned_data

    class Meta:
        model = Placemark
        fields = '__all__'
