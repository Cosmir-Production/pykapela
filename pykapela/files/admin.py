
from django.contrib import admin

from pykapela.files.models import File


@admin.register(File)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')
