from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

from meteleska.base.models import BaseModel


# Create your models here.
class Event(BaseModel):

    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    datetime = models.DateTimeField(verbose_name='Datum a čas')
    description = HTMLField(default='')

    slug = models.SlugField()
    is_published = models.DateTimeField(auto_now_add=True, blank=True)
    is_promoted = models.IntegerField(default=False)
