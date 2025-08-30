from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Notification


# Notification.
@admin.register(Notification)
class NotificationAdmin(ModelAdmin):
    list_display = ("recipient", "channel", "status", "created_at", "sent_at")
    list_filter = ("channel", "status")
    search_fields = ("recipient__username", "recipient__email", "message")