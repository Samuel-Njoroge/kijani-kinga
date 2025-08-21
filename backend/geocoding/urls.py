from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet

# Router
router = DefaultRouter()

# Routes
router.register(r'location', LocationViewSet, basename='location')

urlpatterns = [
    path('', include(router.urls)),
]