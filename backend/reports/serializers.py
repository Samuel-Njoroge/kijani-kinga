from rest_framework import serializers
from .models import Report, ReportMedia


# Report Serializer
class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ['id', 'reporter', 'title', 'description', 'status', 'location', 'created_at', 'updated_at']
        read_only_fields = ['id', 'reporter', 'status', 'created_at', 'updated_at']


# Report Media Serializer
class ReportMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportMedia
        fields = ['id', 'report', 'media', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']

        