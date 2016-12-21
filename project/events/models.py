from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from tinymce.models import HTMLField

from project.base.models import BaseModel


class Event(BaseModel):

    title = models.CharField(max_length=256, verbose_name='admin-title')
    name = models.CharField(max_length=256, verbose_name='admin-name')
    datetime = models.DateTimeField(verbose_name='admin-datetime')
    perex = HTMLField(default='', verbose_name=_('admin-events-perex'))
    description = HTMLField(default='', verbose_name=_('admin-events-description'))
    venue = models.CharField(default='', max_length=256, verbose_name=_('admin-events-venue'))

    slug = models.SlugField()
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
