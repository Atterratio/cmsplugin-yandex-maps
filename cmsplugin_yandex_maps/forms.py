import re

from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.forms import NON_FIELD_ERRORS
from django.utils.translation import ugettext_lazy as _

from .models import YandexMaps, Placemark, Collection, Claster, Route



class ColorInput(forms.TextInput):
    input_type = 'color'



class YandexMapsForm(forms.ModelForm):
    zoom = forms.IntegerField(label=_('Zoom'), initial=12, min_value=0, max_value=23)
    min_zoom = forms.IntegerField(label=_('Minimum zoom'), initial=0, min_value=0, max_value=23)
    max_zoom = forms.IntegerField(label=_('Maximum zoom'), initial=23, min_value=0, max_value=23)

    center_lt = forms.DecimalField(label=_('Latitude'), initial=55.76, min_value=-90, max_value=90, decimal_places=15)
    center_lg = forms.DecimalField(label=_('Longitude'), initial=37.64, min_value=-180, max_value=180, decimal_places=15)

    width = forms.IntegerField(label=_('Width'), initial=320, min_value=1)
    height = forms.IntegerField(label=_('Height'), initial=180, min_value=1)
    jq_selector = forms.CharField(label=_('jQuery selector'), required=False)


    def clean_jq_selector(self):
        jq_selector = self.cleaned_data['jq_selector']

        return jq_selector.replace('"', "'").strip("'")


    def clean(self):
        cleaned_data = super(YandexMapsForm, self).clean()
        auto_placement = cleaned_data['auto_placement']
        data = self.data
        size_update_method = cleaned_data['size_update_method']
        jq_selector = cleaned_data['jq_selector']
        jq_event = cleaned_data['jq_event']

        if auto_placement:
            routes = 0
            pattern = re.compile("yandexmaps_routes_set-\d+-id")
            delete = re.compile("yandexmaps_routes_set-\d+-DELETE")
            for key in data:
                if pattern.match(key):
                    routes += 1

                if delete.match(key):
                    routes -= 1

            if routes > 1:
                self.add_error('auto_placement', _("Don't work with two or more routes"))

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
                                  max_value=90, decimal_places=15)
    place_lg = forms.DecimalField(label=_('Longitude'), required=False, min_value=-180,
                                  max_value=180, decimal_places=15)

    icon_width = forms.IntegerField(label=_('Icon width'), initial=30, min_value=1)
    icon_height = forms.IntegerField(label=_('Icon height'), initial=30, min_value=1)
    icon_offset_horizontal = forms.IntegerField(label=_('Icon offset horizontal'), initial=0)
    icon_offset_vertical = forms.IntegerField(label=_('Icon offset vertical'), initial=0)
    icon_content_offset_horizontal = forms.IntegerField(label=_('Icon content offset horizontal'), initial=0)
    icon_content_offset_vertical = forms.IntegerField(label=_('Icon content offset vertical'), initial=0)

    balloonHeader = forms.CharField(label=_('Balloon header'), widget=forms.Textarea, required=False,
                                    help_text = _("Can use some html, please be careful!"))
    balloonBody = forms.CharField(label=_('Balloon body'), widget=forms.Textarea, required=False,
                                    help_text = _('Replace "Balloon content". Can use some html, please be careful!'))
    balloonFooter = forms.CharField(label=_('Balloon footer'), widget=forms.Textarea, required=False,
                                    help_text = _("Can use some html, please be careful!"))


    def clean_balloonHeader(self):
        balloonHeader = self.cleaned_data['balloonHeader']
        balloonHeader = balloonHeader.replace("'", '"').replace('\n', '<br>')
        
        return balloonHeader


    def clean_balloonBody(self):
        balloonBody = self.cleaned_data['balloonBody']
        balloonBody = balloonBody.replace("'", '"').replace('\r\n', '<br>').replace('\t', '')
        
        return balloonBody


    def clean_balloonFooter(self):
        balloonFooter = self.cleaned_data['balloonFooter']
        balloonFooter = balloonFooter.replace("'", '"').replace('\n', '<br>')

        return balloonFooter


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
        icon_caption = cleaned_data['icon_caption']
        if icon_style == "image" and not icon_image:
            self.add_error('icon_image', forms.ValidationError(forms.fields.Field.default_error_messages['required']))
        elif icon_style in ("", "default", "glif") and icon_caption:
            self.add_error('icon_caption', _("Can't be checked with this style"))
        elif icon_style == "stretchy" and not icon_caption:
            self.add_error('icon_caption', _("Must be checked with this style"))

        return cleaned_data


    class Meta:
        model = Placemark
        fields = '__all__'



class CollectionForm(forms.ModelForm):
    icon_width = forms.IntegerField(label=_('Icon width'), initial=30, min_value=1)
    icon_height = forms.IntegerField(label=_('Icon height'), initial=30, min_value=1)
    icon_offset_horizontal = forms.IntegerField(label=_('Icon offset horizontal'), initial=0)
    icon_offset_vertical = forms.IntegerField(label=_('Icon offset vertical'), initial=0)
    icon_content_offset_horizontal = forms.IntegerField(label=_('Icon content offset horizontal'), initial=0)
    icon_content_offset_vertical = forms.IntegerField(label=_('Icon content offset vertical'), initial=0)


    def clean(self):
        cleaned_data = super(CollectionForm, self).clean()

        icon_style = cleaned_data['icon_style']
        icon_image = cleaned_data['icon_image']
        icon_caption = cleaned_data['icon_caption']
        if icon_style == "image" and not icon_image:
            self.add_error('icon_image', forms.ValidationError(forms.fields.Field.default_error_messages['required']))
        elif icon_style in ("", "default", "glif") and icon_caption:
            self.add_error('icon_caption', _("Can't be checked with this style"))
        elif icon_style == "stretchy" and not icon_caption:
            self.add_error('icon_caption', _("Must be checked with this style"))

        return cleaned_data


    class Meta:
        auto_created = True
        model = Collection
        fields = '__all__'



class ClasterForm(forms.ModelForm):
    icon_width = forms.IntegerField(label=_('Icon width'), initial=30, min_value=1)
    icon_height = forms.IntegerField(label=_('Icon height'), initial=30, min_value=1)
    icon_offset_horizontal = forms.IntegerField(label=_('Icon offset horizontal'), initial=0)
    icon_offset_vertical = forms.IntegerField(label=_('Icon offset vertical'), initial=0)
    icon_content_offset_horizontal = forms.IntegerField(label=_('Icon content offset horizontal'), initial=0)
    icon_content_offset_vertical = forms.IntegerField(label=_('Icon content offset vertical'), initial=0)


    def clean(self):
        cleaned_data = super(ClasterForm, self).clean()

        icon_style = cleaned_data['icon_style']
        icon_image = cleaned_data['icon_image']
        icon_caption = cleaned_data['icon_caption']
        if icon_style == "image" and not icon_image:
            self.add_error('icon_image', forms.ValidationError(forms.fields.Field.default_error_messages['required']))
        elif icon_style in ("", "default", "glif") and icon_caption:
            self.add_error('icon_caption', _("Can't be checked with this style"))
        elif icon_style == "stretchy" and not icon_caption:
            self.add_error('icon_caption', _("Must be checked with this style"))

        return cleaned_data


    class Meta:
        model = Claster
        fields = '__all__'



class RouteForm(forms.ModelForm):
    results = forms.IntegerField(label=_('Results'), initial=1, min_value=1)

    route_collor = forms.CharField(widget=ColorInput, label=_('Route collor'), initial="#9635ba")
    additional_routes_collor = forms.CharField(widget=ColorInput, label=_('Additional routes collor'), initial="#7a684e")


    def clean(self):
        cleaned_data = super(RouteForm, self).clean()
        data = self.data

        placemarks = 0
        pattern = re.compile("route_placemarks_set-\d+-id")
        delete = re.compile("route_placemarks_set-\d+-DELETE")
        for key in data:
            if pattern.match(key):
                placemarks += 1

            if delete.match(key):
                placemarks -= 1

        if placemarks < 2:
            self.add_error(NON_FIELD_ERRORS, _("To create route need at least two Placemarks"))

        return cleaned_data


    class Meta:
        model = Route
        fields = '__all__'