import os.path

from cms.models import CMSPlugin
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import pgettext_lazy, ungettext_lazy
from django.utils.translation import ugettext_lazy as _
from unidecode import unidecode


COLORS = (('blue', _('Blue')), ('red', _('Red')), ('darkOrange', _('Dark orange')), ('night', _('Night')),
          ('darkBlue', _('DarkBlue')), ('pink', _('Pink')), ('gray', _('Gray')), ('brown', _('Brown')),
          ('darkGreen', _('Dark green')), ('violet', _('Violet')), ('black', _('Black')), ('yellow', _('Yellow')),
          ('green', _('Green')), ('orange', _('Orange')), ('lightBlue', _('Light blue')), ('olive', _('Olive')))



class YandexMaps(CMSPlugin):
    """
    A yandex maps integration
    """
    title = models.CharField(_("Map title"), max_length=140, blank=True, null=True)
    MAP_TYPES = (('map', _('Scheme')),
                 ('satellite', _('Satellite')),
                 ('hybrid', _('Hybryd')))
    map_type = models.CharField(_('Initial type'), max_length=10, choices=MAP_TYPES, default='map')

    route = models.BooleanField(_('Create route'), default=False,
                                help_text = _('Create route between points (unstable)'))

    clusterisation = models.BooleanField(_('Clusterisation'), default=True)
    cluster_disable_click_zoom = models.BooleanField(_('Disable cluster click zoom'), default=True)
    CLUSTER_ICON = (('default', _('Default')), ('inverted', _('Inverted')))
    cluster_icon = models.CharField(_('Cluster icon'), max_length=8, choices=CLUSTER_ICON,
                                    default='default')
    cluster_color = models.CharField(_('Cluster icon color'), max_length=15, choices=COLORS,
                                     default='red')

    LANG = (('ru_RU', 'Русский'),
            ('en_RU', 'English'),
            ('uk_UA', 'Українська'),
            ('tr_TR', 'Türk'))
    lang = models.CharField(_('Language'), max_length=5, choices=LANG, default='ru_RU')

    auto_placement = models.BooleanField(_('Auto placement'), default=True,
                                         help_text = _('Automatically find the center and zoom'))
    zoom = models.IntegerField(_('Zoom'), default=12)
    min_zoom = models.IntegerField(_('Minimum zoom'), default=0)
    max_zoom = models.IntegerField(_('Maximum zoom'), default=23)
    center_lt = models.FloatField(_('Latitude'), default=55.76)
    center_lg = models.FloatField(_('Longitude'), default=37.64)

    SIZING = (('aspect', _('Keep aspect')),
              ('static', _('Static')),
              ('auto', pgettext_lazy('Like automatisation', 'Auto')))
    sizing = models.CharField(_('Sizing'), max_length=6, choices=SIZING, default='aspect')
    width = models.IntegerField(_('Width'), default=320)
    height = models.IntegerField(_('Height'), default=180)
    UPDATE_METHOD = (('observer', 'MutationObserver'),
                     ('jq_event', _('jQuery event')))
    size_update_method = models.CharField(_('Size update method'), max_length=8,
                                          choices=UPDATE_METHOD, blank=True, null=True,
                                          help_text = _('MutationObserver may be slow,not all events work, enable only if work not proper with hidden object'))
    jq_selector = models.CharField(_('jQuery selector'), max_length=300, blank=True, null=True)
    JQ_EVENTS = (('blur', 'Blur'), ('change', 'Change'), ('click', 'Click'),
                 ('contextmenu', 'Contextmenu'), ('dblclick', 'Dblclick'), ('focus', 'Focus'),
                 ('focusin', 'Focusin'), ('focusout', 'Focusout'), ('hover', 'Hover'),
                 ('keydown', 'Keydown'), ('keypress', 'Keypress'), ('keyup', 'Keyup'),
                 ('load', 'Load'), ('mousedown', 'Mousedown'), ('mouseenter', 'Mousedown'),
                 ('mouseleave', 'Mouseleave'), ('mousemove', 'Mousemove'), ('mouseout', 'Mouseout'),
                 ('mouseover', 'Mouseover'), ('mouseup', 'Mouseup'), ('scroll', 'Scroll'),
                 ('select', 'Select'), ('submit', 'Submit'))
    jq_event = models.CharField(_('jQuery event'), max_length=15, choices=JQ_EVENTS, default='click')

    behaviors = models.ManyToManyField('Behavior', verbose_name=_('Behaviors'),
                                       default=(1, 2, 3, 4, 6), blank=True,
                                       help_text = _("Sorry for the Russian, I'm too lazy and just copied the description from the documentation"))

    controls = models.ManyToManyField('Control', verbose_name=_('Controls'),
                                      default=(5, 6, 7), blank=True,
                                      help_text = _("Sorry for the Russian, I'm too lazy and just copied the description from the documentation"))

    classes = models.TextField(verbose_name=_('CSS classes'), blank=True)
    
    placemarks = models.ManyToManyField('Placemark', blank=True,
                                        verbose_name=ungettext_lazy("Placemark", "Placemarks", 1))


    @property
    def cluster_preset(self):
        if self.cluster_icon == 'default':
            return "islands#%sClusterIcons" % self.cluster_color
        elif self.cluster_icon == 'inverted':
            return "islands#inverted%sClusterIcons" % self.cluster_color.capitalize()


    def copy_relations(self, oldinstance):
        self.behaviors = oldinstance.behaviors.all()
        self.controls = oldinstance.controls.all()
        self.placemarks = self.placemarks.all()
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = _("Yandex Maps")
        verbose_name_plural = _("Yandex Maps")



class Behavior(models.Model):
    behavior = models.CharField(_("Behavior"), max_length=30, unique=True)
    description = models.CharField(_("Description"), max_length=300, blank=True, null=True)

    def __str__(self):
        return "%s | %s" % (self.behavior, self.description)



class Control(models.Model):
    control = models.CharField(_("Control"), max_length=30, unique=True)
    description = models.CharField(_("Description"), max_length=300, blank=True, null=True)

    def __str__(self):
        return "%s | %s" % (self.control, self.description)



def upload_path_handler(instance, filename):
    fn, ext = os.path.splitext(filename)
    path = 'cmsplugin_yandex_maps/placemarks/%(fn)s.%(ext)s' % {
            'fn': slugify(unidecode(fn)), 'ext': slugify(unidecode(ext))}

    return path



class Placemark(models.Model):
    title = models.CharField(_("Title"), max_length=50, blank=True, null=True)

    auto_coordinates = models.BooleanField(_('Auto coordinates'), default=True)
    place = models.CharField(_("Place"), max_length=300, blank=True, null=True)
    place_lt = models.FloatField(_('Latitude'), blank=True, null=True)
    place_lg = models.FloatField(_('Longitude'), blank=True, null=True)

    icon_color = models.CharField(_('Marker icon color'), max_length=15, choices=COLORS,
                                  default='red')
    ICON_STYLE = (('default', _('Default')), ('stretchy', _('Stretchy')), ('doted', _('Doted')),
                  ('glif', _('With glif')), ('image', _('Image')))
    icon_style = models.CharField(_('Marker icon style'), max_length=8, choices=ICON_STYLE, default='default')
    icon_circle = models.BooleanField(_('Circle icon'), default=False)
    icon_caption = models.BooleanField(_('Caption'), default=False)
    ICON_GLIF = (('Home', _('Home')), ('Airport', _('Airport')), ('Bar', _('Bar')), ('Food', _('Food')),
                 ('Cinema', _('Cinema')), ('MassTransit', _('Mass Transit')), ('Toilet', _('Toilet')), ('Beach', _('Beach')),
                 ('Zoo', _('Zoo')), ('Underpass', _('Underpass')), ('Run', _('Run')), ('Bicycle', _('Bicycle')), ('Bicycle2', _('Bicycle2')),
                 ('Garden', _('Garden')), ('Observation', _('Observation')), ('Entertainment', _('Entertainment')),
                 ('Family', _('Family')), ('Theater', _('Theater')), ('Book', _('Book')), ('Waterway', _('Waterway')),
                 ('RepairShop', _('Repair Shop')), ('Post', _('Post')), ('WaterPark', _('Water Park')), ('Worship', _('Worship')),
                 ('Fashion', _('Fashion')), ('Waste', _('Waste')), ('Money', _('Money')), ('Hydro', _('Hydro')),
                 ('Science', _('Science')), ('Auto', pgettext_lazy('Like Car', 'Auto')), ('Shopping', _('Shopping')), ('Sport', _('Sport')),
                 ('Video', _('Video')), ('Railway', _('Railway')), ('Park', _('Park')), ('Pocket', _('Pocket')),
                 ('NightClub', _('Night Club')), ('Pool', _('Pool')), ('Medical', _('Medical')), ('Vegetation', _('Vegetation')),
                 ('Government', _('Government')), ('Circus', _('Circus')), ('RapidTransit', _('Rapid Transit')), ('Education', _('Education')),
                 ('Mountain', _('Mountain')), ('CarWash', _('Car Wash')), ('Factory', _('Factory')), ('Court', _('Court')),
                 ('Hotel', _('Hotel')), ('Christian', _('Christian')), ('Laundry', _('Laundry')), ('Souvenirs', _('Souvenirs')),
                 ('Dog', _('Dog')), ('Leisure', _('Leisure')))
    icon_glif = models.CharField(_('Icon glif'), max_length=30, choices=ICON_GLIF, default='Home')
    icon_image = models.ImageField(_('Icon image'), max_length=500, blank=True, null=True,
                                    upload_to=upload_path_handler)
    icon_width = models.IntegerField(_('Icon width'), default=30)
    icon_height = models.IntegerField(_('Icon height'), default=30)
    icon_offset_horizontal= models.IntegerField(_('Icon offset horizontal'), default=0)
    icon_offset_vertical = models.IntegerField(_('Icon offset vertical'), default=0)
    icon_content_offset_horizontal= models.IntegerField(_('Icon content offset horizontal'), default=0)
    icon_content_offset_vertical = models.IntegerField(_('Icon content offset vertical'), default=0)

    hint = models.CharField(_("Placemark hint"), max_length=140, blank=True, null=True)

    balloon = models.CharField(_("Balloon content"), max_length=300, blank=True, null=True)
    balloonHeader = models.TextField(_('Balloon header'), blank=True,
                                    help_text = _("Can use some html, please be careful!"))
    balloonBody = models.TextField(_('Balloon body'), blank=True,
                                    help_text = _('Replace "Balloon content". Can use some html, please be careful!'))
    balloonFooter = models.TextField(_('Balloon footer'), blank=True,
                                    help_text = _("Can use some html, please be careful!"))


    @property
    def marker_preset(self):
        if self.icon_style == 'default':
            if self.icon_circle:
                return "islands#%(color)sCircleIcon" % {'color': self.icon_color}
            else:
                return "islands#%(color)sIcon" % {'color': self.icon_color}

        elif self.icon_style == 'stretchy':
            return "islands#%(color)sStretchyIcon" % {'color': self.icon_color}
        elif self.icon_style == 'doted':
            if self.icon_circle and self.icon_caption:
                return "islands#%(color)sCircleDotIconWithCaption" % {'color': self.icon_color}
            elif self.icon_circle:
                return "islands#%(color)sCircleDotIcon" % {'color': self.icon_color}
            elif self.icon_caption:
                return "islands#%(color)sDotIcon" % {'color': self.icon_color}
            else:
                return "islands#%(color)sDotIconWithCaption" % {'color': self.icon_color}
        elif self.icon_style == 'glif':
            if self.icon_circle:
                return "islands#%(color)s%(glif)sCircleIcon" % {'color': self.icon_color, 'glif': self.icon_glif}
            else:
                return "islands#%(color)s%(glif)sIcon" % {'color': self.icon_color, 'glif': self.icon_glif}


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = ungettext_lazy("Placemark", "Placemarks", 1)
        verbose_name_plural = ungettext_lazy("Placemark", "Placemarks", 2)



@receiver(pre_save, sender=Placemark)
def delete_old_image(instance, **kwargs):
    if instance.id:
        old_instance = kwargs['sender'].objects.get(id=instance.id)
        if old_instance.icon_image and old_instance.icon_image != instance.icon_image:
            try:
                os.remove('%s/%s' % (settings.MEDIA_ROOT, old_instance.icon_image))
            except:
                pass



@receiver(post_delete, sender=Placemark)
def cleanup_image(instance, **kwargs):
    if instance.id:
        try:
            os.remove('%s/%s' % (settings.MEDIA_ROOT, instance.icon_image))
        except:
            pass