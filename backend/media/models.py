from django.db import models
from django.conf import settings
import uuid


# Media.
class Media(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('audio', 'Audio'),
        ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    file = models.FileField()
    media_type = models.CharField(max_length=25, choices=MEDIA_TYPES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.file}"
    
    class Meta:
        db_table = 'media'
        verbose_name = 'Media'
        verbose_name_plural = 'Media'
