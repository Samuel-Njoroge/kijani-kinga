from django.db import models
import uuid
from django.conf import settings
from geocoding.models import Location
from media.models import Media


# Report
class Report(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('closed', 'Closed'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='report')
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    is_public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} is {self.status}"
    
    class Meta:
        db_table = 'reports'
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'


# Report Media
class ReportMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='reports')
    media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='media')
    description = models.TextField()

    def __str__(self):
        return f"{self.id} contains {self.report}"

    class Meta:
        db_table = 'report_media'
        verbose_name = 'Report Media'
        verbose_name_plural = 'Report Media'
