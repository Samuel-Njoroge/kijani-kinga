from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from geopy.geocoders import Nominatim
from .models import Location
from .serializers import LocationSerializer


# Location
geolocator = Nominatim(user_agent="kijani_kinga")

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def reverse_lookup(self, request):
        lat = request.query_params.get('lat')
        lng = request.query_params.get('lng')
        if not lat or not lng:
            return Response({"error": "lat and lng are required"}, status=400)
        
        location = geolocator.reverse((lat, lng), language="en")
        return Response({
            "latitude": lat,
            "longitude": lng,
            "address": location.address if location else None
        })