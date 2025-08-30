from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer


# Notification
class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.all().order_by("-created_at")
    serializer_class = NotificationSerializer