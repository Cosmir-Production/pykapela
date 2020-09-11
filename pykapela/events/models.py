from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from tinymce.models import HTMLField

from pykapela.base.models import BaseModel


class Event(BaseModel):

    # mandatory fields
    title = models.CharField(_('Venue name'), max_length=256, help_text='Create nice name for this venue! No location here.')
    datetime = models.DateTimeField(verbose_name='Starts at')

    location = models.CharField(max_length=256, default='', blank=True, verbose_name=_('Name of a club or festival'))
    address = models.CharField(max_length=256, verbose_name='Where is it?', blank=True)

    description = HTMLField(default='', blank=True, verbose_name=_('Event description (optional)'))

    slug = models.SlugField('URL slug', help_text='Use only small caps, no spaces, just hyphens. Must be unique.')
    is_published = models.BooleanField(default=True)
    is_promoted = models.BooleanField(default=False,
                                      help_text=_('Promoted events will be first. Otherwise sorted by datetime'))

    image = models.ImageField(
        upload_to='images/concerts/',
        verbose_name=_('Image'),
        null=True,
        blank=True,
    )

    IMAGE_GEOMETRY = {
        'small': ('400x', None),
        'medium': ('900x', None),
        'large': ('900x', None),
        'bandzone': ('518x900', None),
    }

    def __str__(self):
        return self.title + ' @ ' + self.location

    def admin_title(self):
        return self.title + ' @ ' + self.location
