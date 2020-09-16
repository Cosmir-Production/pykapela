from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from pykapela.base.models import BaseModel


class File(BaseModel):

    name = models.CharField(max_length=256, blank=True)

    file = models.FileField(
        upload_to="files",
        help_text=_('Upload your file here'),
    )

    def __str__(self):
        return self.name

    def save(self):

        if self.name == '':
            self.name = self.file.name

        return super().save()