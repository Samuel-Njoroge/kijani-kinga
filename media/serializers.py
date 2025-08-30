from rest_framework import serializers
from .models import Media


# Media Serializer
class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = '__all__'