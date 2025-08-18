from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import User, UserProfile


# User
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ()
    search_fields = ()
    list_filter = ()


# User Profile
@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ()
    search_fields = ()
    list_filter = ()