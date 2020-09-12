from __future__ import unicode_literals
from tinymce.models import HTMLField

from django.db import models
from django.utils.translation import ugettext as _

from pykapela.base.models import BaseModel


class Page(BaseModel):

    title = models.CharField(max_length=256)
    content = HTMLField(default='', blank=True)

    slug = models.SlugField(null=True, blank=True, help_text='Modules available: '
                                                             'homepage, events, music, news, gallery, bio, contact, '
                                                             'Add these pages with equivalent position '
                                                             'to match background images.')
    is_published = models.BooleanField(default=True)

    position = models.IntegerField(default=1, help_text=_('Background images on homepage are sorted by position.'))

    is_dark = models.BooleanField(default=True, help_text=_('Dark background and white font color.'))

    image = models.ImageField(
        upload_to='images/pages/',
        verbose_name=_('Main Image'),
        null=True,
        blank=True
    )

    IMAGE_GEOMETRY = {
        'large': ('1080x', None),
    }

    portrait_image = models.ImageField(
        upload_to='images/pages/',
        verbose_name=_('Portrait Image (optional)'),
        null=True,
        blank=True
    )

    PORTRAIT_IMAGE_GEOMETRY = {
        'large': ('1080x', None),
    }

    def __str__(self):
        return self.title
