from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from pykapela.base.models import BaseModel
from pykapela.preferences import choices


class Preference(BaseModel):

    site_name = models.CharField(max_length=256)
    slogan = models.CharField(max_length=255, default='', blank=True, help_text='Optional.')
    description = models.CharField(max_length=255, default='', blank=True, help_text='Optional.')
    footer_slogan = models.CharField(max_length=255, default='', blank=True, help_text='Optional.')
    footer_copyright = models.CharField(max_length=255, default='', blank=True, help_text='Optional.')

    promoted_gallery = models.IntegerField(default=1, help_text='ID of gallery to be promoted on homepage.')

    email = models.CharField(max_length=60, default='')
    phone = models.CharField(max_length=32, default='')

    favicon = models.FileField(
        upload_to="images/",
        verbose_name="Favicon",
        help_text=_("User some generator to create your favicon.ico file."),
        null=True,
        blank=True,
    )

    logo = models.ImageField(
        upload_to='images/logo/',
        verbose_name=_('Logo'),
        null=True,
        blank=True,
    )

    IMAGE_GEOMETRY = {
        'large': ('420x', None),
    }

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
                footer_slogan='',
            ).save()
            preferences = Preference.objects.get(pk=1)

        result = {}
        for key in preferences._meta.fields:
            result.update({
                'config_' + str(key.column): getattr(preferences, str(key.column)),
            })
        return result

