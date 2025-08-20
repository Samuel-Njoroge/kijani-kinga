from rest_framework import viewsets, permissions
from .models import Media
from .serializers import MediaSerializer 


# Media ViewSet
class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [permissions.IsAuthenticated]

