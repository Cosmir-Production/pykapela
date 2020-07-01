
from django.db import models
from django.utils.translation import ugettext as _


class BaseModel(models.Model):

    created = models.DateTimeField(
        auto_now_add=True, editable=False, db_index=True,
        verbose_name=_('admin-base-base-time-model-created')
    )
    changed = models.DateTimeField(
        auto_now=True, editable=False, db_index=True,
        verbose_name=_('admin-base-base-time-model-changed')
    )

    class Meta:
        abstract = True


class BaseManager(models.Manager):
    pass
