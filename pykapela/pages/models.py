from __future__ import unicode_literals
from tinymce.models import HTMLField

from django.db import models
from django.utils.translation import ugettext as _

from pykapela.base.models import BaseModel


class Page(BaseModel):

    title = models.CharField(max_length=256)
    content = HTMLField(default='', blank=True)

    slug = models.SlugField(null=True, blank=True)
    is_published = models.BooleanField(default=True)

    position = models.IntegerField(default=1)

    image = models.ImageField(
        upload_to='images/pages/',
        verbose_name=_('admin-pages-image'),
        null=True,
        blank=True
    )

    IMAGE_GEOMETRY = {
        'large': ('1080x', None),
    }

    def __str__(self):
        return self.title
