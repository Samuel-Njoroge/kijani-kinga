from django.db import models
import uuid
from reports.models import Report
from django.conf import settings

# Notification
class Notification(models.Model):
    CHANNEL = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]
    STATUS = [
        ('sent', 'Sent'),
        ('pending', 'Pending'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    channel = models.CharField(max_length=25, choices=CHANNEL)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=25, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.channel.upper()} → {self.recipient.email} [{self.status}]"
    
    class Meta:
        db_table = 'notification'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
