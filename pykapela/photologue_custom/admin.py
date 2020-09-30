from django.contrib import admin
from django.utils.safestring import mark_safe

from photologue.admin import GalleryAdmin as GalleryAdminDefault, PhotoAdmin as PhotoAdminDefault, GalleryAdminForm
from photologue.models import Gallery, Photo
from .models import GalleryExtended


class GalleryExtendedInline(admin.StackedInline):
    model = GalleryExtended
    can_delete = False


class PykapelaGalleryAdminForm(GalleryAdminForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # change title to img url on gallery edits
        photos = Photo.objects.all()
        items = []
        for photo in photos:
            items.append(
                (photo.pk, mark_safe('%s' % photo.image.url))
            )
        self.fields['photos'].choices = items


class GalleryAdmin(GalleryAdminDefault):

    """Define our new one-to-one model as an inline of Photologue's Gallery model."""
    form = PykapelaGalleryAdminForm
    inlines = [GalleryExtendedInline, ]


class PhotoAdmin(PhotoAdminDefault):
    list_display = ('title', 'date_taken', 'date_added',
                    'is_public', 'view_count', 'caption', 'admin_thumbnail')
    list_filter = ['date_added', 'is_public', 'galleries']


admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)

admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin)
