from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Report, ReportMedia


# Report.
@admin.register(Report)
class ReportAdmin(ModelAdmin):
    list_display = ('title', 'reporter', 'location', 'status',)
    search_fields = ('location', 'title')
    list_filter = ('status',)


# Report Media.
@admin.register(ReportMedia)
class ReportMediaAdmin(ModelAdmin):
    list_display = ('report', 'media', 'description')
    search_fields = ('report',)
    list_filter = ('report',)
