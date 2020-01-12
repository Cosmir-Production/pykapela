from __future__ import unicode_literals

from django.db import models

from project.base.models import BaseModel


class Social(BaseModel):

    title = models.CharField(max_length=256)
    name = models.CharField(max_length=56, verbose_name='System name, "facebook" for example')
    url = models.CharField(max_length=256)
    secret_key = models.CharField(max_length=256, blank=True, default='')
    is_promoted = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    position = models.IntegerField(default=0)
    widget_code = models.TextField(default='', blank=True)
