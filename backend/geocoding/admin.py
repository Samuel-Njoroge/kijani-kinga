from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Location

# Media.
@admin.register(Location)
class LocationAdmin(ModelAdmin):
    list_display = ('id', 'country', 'region', 'latitude', 'longitude', 'created_at')
    search_fields = ('report', 'country')
    list_filter = ('report',)
