from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

from pykapela.base.models import BaseModel


class Page(BaseModel):

    title = models.CharField(max_length=256)
    content = HTMLField(default='')

    slug = models.SlugField()
    is_published = models.BooleanField(default=True)
