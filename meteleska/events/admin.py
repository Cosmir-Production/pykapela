
from django.contrib import admin

from meteleska.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
