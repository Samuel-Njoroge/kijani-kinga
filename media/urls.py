from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaViewSet

# Router
router = DefaultRouter()

# Routes
router.register(r'media', MediaViewSet, basename='media')

urlpatterns = [
    path('', include(router.urls)),
]