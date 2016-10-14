from __future__ import unicode_literals

from django.db import models

from meteleska.base.models import BaseModel


# Create your models here.
class Event(BaseModel):
    name = models.CharField()
