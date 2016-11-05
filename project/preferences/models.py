from __future__ import unicode_literals

from django.db import models

from project.base.models import BaseModel
from project.preferences import choices


class Preference(BaseModel):

    name = models.CharField(max_length=256)
    type = models.IntegerField(
        choices=choices.PREFERENCES_TYPES,
        default=0,
    )
    content = models.TextField(default='')
