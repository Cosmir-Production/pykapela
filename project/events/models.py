from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from tinymce.models import HTMLField

from project.base.models import BaseModel


class Event(BaseModel):

    # mandatory fields
    title = models.CharField(max_length=256, verbose_name='Title')
    datetime = models.DateTimeField(verbose_name='Starts at')

    location = models.CharField(max_length=256, default='', blank=True, verbose_name=_('Name of a club or festival'))
    address = models.CharField(max_length=256, verbose_name='Address', blank=True)

    description = HTMLField(default='', blank=True, verbose_name=_('Event description (optional)'))

    slug = models.SlugField('URL slug')
    is_published = models.BooleanField(default=True)
    is_promoted = models.BooleanField(default=False)

    image = models.ImageField(
        upload_to='images/concerts/',
        verbose_name=_('admin-events-image'),
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
