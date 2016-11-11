from __future__ import unicode_literals

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.translation import ugettext as _

from tinymce.models import HTMLField

from project.base.models import BaseModel
from project.base.utils import get_uuid


class ImageStorage(FileSystemStorage):
    pass


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

    def upload_to(self):
        return u'concerts/{image_name}'.format(
            image_name=get_uuid(),
        )

    image = models.ImageField(
        upload_to=upload_to,
        verbose_name=_('admin-events-image'),
        storage=ImageStorage(
            location=settings.IMAGE_ROOT,
            base_url=settings.IMAGE_URL
        ),
        null=True,
    )

    IMAGE_GEOMETRY = {
        'small': ('400x', None),
        'medium': ('900x', None),
        'large': ('900x', None),
        'bandzone': ('518x900', None),
    }
