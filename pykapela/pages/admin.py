
from django.contrib import admin

from pykapela.pages.models import Page


@admin.register(Page)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'is_published')
