
from django.contrib import admin

from pykapela.preferences.models import Preference


@admin.register(Preference)
class PreferencesAdmin(admin.ModelAdmin):
    list_display = ('site_name', )
