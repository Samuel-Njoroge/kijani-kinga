from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


# User
class User(AbstractUser):
    ROLE_CHOICES = [
        ('resident', 'Resident'),
        ('ranger', 'Ranger'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='resident')

    def __str__(self):
        return f"{self.username} ({self.role})"
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    

# User Profile
class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'