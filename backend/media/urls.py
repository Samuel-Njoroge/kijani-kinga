from django.urls import path, include
from rest_framework.router import DefaultRouter
from .views import MediaViewSet

# Router
router = DefaultRouter()

# Routes
router.register(r'media', MediaViewSet, basename='media')

urlpatterns = [
    path('', include(router.urls)),
]