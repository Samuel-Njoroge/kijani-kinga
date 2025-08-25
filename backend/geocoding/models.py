from django.db import models
import uuid


# Location
class Location(models.Model):
    SOURCES = [
        ('gps', 'GPS'),
        ('manual', 'Manual')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    country = models.CharField(max_length=25)
    region = models.CharField(max_length=25)
    address = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=25, choices=SOURCES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report} reported in {self.country}, {self.region}"
    
    class Meta:
        db_table = 'location'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    
