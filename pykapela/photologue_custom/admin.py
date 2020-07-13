from django.contrib import admin

from photologue.admin import GalleryAdmin as GalleryAdminDefault, PhotoAdmin
from photologue.models import Gallery, Photo
from .models import GalleryExtended


class GalleryExtendedInline(admin.StackedInline):
    model = GalleryExtended
    can_delete = False


class GalleryAdmin(GalleryAdminDefault):

    """Define our new one-to-one model as an inline of Photologue's Gallery model."""

    inlines = [GalleryExtendedInline, ]


class PhotoAdmin(PhotoAdmin):

    list_display = ('title', 'date_taken', 'date_added',
                    'is_public', 'view_count', 'caption', 'admin_thumbnail')
    list_filter = ['date_added', 'is_public', 'galleries']


admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)

admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin)
