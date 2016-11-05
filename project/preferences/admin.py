
from django.contrib import admin

from project.preferences.models import Preference


@admin.register(Preference)
class PreferencesAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
