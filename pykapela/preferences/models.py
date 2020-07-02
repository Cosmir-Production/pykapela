from __future__ import unicode_literals

from django.db import models

from pykapela.base.models import BaseModel
from pykapela.preferences import choices


class Preference(BaseModel):

    site_name = models.CharField(max_length=256)
    slogan = models.CharField(max_length=255, default='', help_text='Optional.')

    email = models.CharField(max_length=60, default='')
    phone = models.CharField(max_length=32, default='')

    @staticmethod
    def get_values():

        try:
            preferences = Preference.objects.get(pk=1)
        except Preference.DoesNotExist:
            Preference(
                site_name='My great project!',
                slogan='This site is something special. Come and see.',
                email='put_your@email.here',
                phone='123 456 789',
            ).save()
            preferences = Preference.objects.get(pk=1)

        result = {}
        for key in preferences._meta.fields:
            result.update({
                'config_' + str(key.column): getattr(preferences, str(key.column)),
            })
        return result

