from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportViewSet, ReportMediaViewSet

# Router
router = DefaultRouter()

# Routes
router.register(r'reports', ReportViewSet, basename='reports')
router.register(r'report-media', ReportMediaViewSet, basename='report-media')

urlpatterns = [
    path('', include(router.urls)),
]