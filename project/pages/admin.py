
from django.contrib import admin

from project.pages.models import Page


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
