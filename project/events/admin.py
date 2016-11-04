
from django.contrib import admin

from project.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime', 'is_promoted', 'is_published')
    date_hierarchy = 'datetime'
