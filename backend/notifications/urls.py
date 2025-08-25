from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet
from django.urls import path, include

# Router
router = DefaultRouter()

# Routes
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]