from __future__ import unicode_literals

from django.db import models

from project.base.models import BaseModel
from project.preferences import choices


class Preference(BaseModel):

    site_name = models.CharField(max_length=256)

    @staticmethod
    def get_values():
        result = {}
        preferences = Preference.objects.all().first()
        for key in preferences._meta.fields:
            result.update({
                'config_' + str(key.column): getattr(preferences, str(key.column)),
            })
        return result

