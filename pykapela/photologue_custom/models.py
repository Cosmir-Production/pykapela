from django.conf import settings
from django.db import models

from taggit.managers import TaggableManager

from photologue.models import Gallery


class GalleryExtended(models.Model):

    # Link back to Photologue's Gallery model.
    gallery = models.OneToOneField(Gallery, related_name='extended', null=True, on_delete=models.SET_NULL)

    # This is the important bit - where we add in the tags:
    tags = TaggableManager(blank=True)

    # Boilerplate code to make a prettier display in the admin interface:
    class Meta:
        verbose_name = u'Extra fields'
        verbose_name_plural = u'Extra fields'

    def __str__(self):
        return self.gallery.title


class PykapelaGallery(Gallery):

    class Meta:
        proxy = True

    def latest(self, limit=settings.PHOTOLOGUE_GALLERY_LATEST_LIMIT, public=True):
        if not limit:
            limit = self.photo_count()
        if public:
            return self.public().order_by('-date_added')[:limit]
        else:
            return self.photos.filter(sites__id=settings.SITE_ID)[:limit]
