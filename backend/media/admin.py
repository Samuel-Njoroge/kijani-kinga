from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Media

# Media.
@admin.register(Media)
class MediaAdmin(ModelAdmin):
    list_display = ('id', 'file', 'media_type', 'updloaded_by')
    search_fields = ('file', 'media_type')
    list_filter = ('file',)
