from django.conf import settings
from django.contrib import admin

from pykapela.pages.models import Page


@admin.register(Page)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'is_published')
    fields = tuple('title_' + lang[0] for lang in settings.LANGUAGES) \
             + tuple('content_' + lang[0] for lang in settings.LANGUAGES) \
            + ('slug', 'position', 'is_published', 'image', 'portrait_image')