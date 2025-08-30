from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path, include

# Router
router = DefaultRouter()

# Routes
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]