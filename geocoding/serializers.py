from rest_framework import serializers
from .models import Location


# Location
class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['id', 'latitude', 'longitude', 'address', 'created_at']
        read_only_fields = ['id', 'created_at']