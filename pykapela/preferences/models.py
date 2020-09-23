from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from pykapela.base.models import BaseModel
from pykapela.preferences import choices


class Preference(BaseModel):

    site_name = models.CharField(max_length=256)
    slogan = models.CharField(max_length=255, default='', blank=True, help_text='Optional.')
    title_slogan = models.CharField(max_length=100, default='', blank=True,
                                    help_text="Visible on homepage in browser's title or favourites.")
    description = models.CharField(max_length=255, default='', blank=True,
                                   help_text='Visible in Google on basic search.')
    footer_slogan = models.CharField(max_length=255, default='', blank=True, help_text='Optional.')
    footer_copyright = models.CharField(max_length=255, default='', blank=True, help_text='Optional.')

    promoted_gallery = models.IntegerField(default=1, help_text='ID of gallery to be promoted on homepage.')

    email = models.CharField(max_length=60, default='')
    phone = models.CharField(max_length=32, default='')

    show_languages = models.BooleanField(default=True, help_text=_('Show languages menu on top?'))

    primary_color = models.CharField(max_length=16, default='#000000')
    secondary_color = models.CharField(max_length=16, default='#c0c0c0')

    custom_css = models.TextField(default='', blank=True)

    rider_file = models.FileField(
        upload_to="files/",
        verbose_name=_("Rider"),
        help_text=_("Rider - technical and other demands for promoters."),
        null=True,
        blank=True,
    )

    press_zip_file = models.FileField(
        upload_to="files/",
        verbose_name=_("Press Photos"),
        help_text=_("ZIP file with high quality photos."),
        null=True,
        blank=True,
    )

    logo_file = models.FileField(
        upload_to="files/",
        verbose_name=_("Logo for download."),
        null=True,
        blank=True,
    )

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

    google_analytics = models.TextField(default='', blank=True)

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

