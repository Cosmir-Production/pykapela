
from django.contrib import admin

from pykapela.social.models import Social


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'is_promoted', 'position')
