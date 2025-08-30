from rest_framework import serializers
from .models import Report, ReportMedia
from media.models import Media
from media.serializers import MediaSerializer


# Report Media Serializer
class ReportMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportMedia
        fields = ['id', 'report', 'media']


# Report Serializer
class ReportSerializer(serializers.ModelSerializer):
    media_files = MediaSerializer(many=True, write_only=True, required=False)
    attached_media = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ['id', 'reporter', 'title', 'description', 'status', 'created_at', 'updated_at', 'attached_media', 'media_files']
        read_only_fields = ['id', 'reporter', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        media_files = validated_data.pop('media_files', [])
        report = Report.objects.create(**validated_data, user=self.context['request'].user)

        # Save media and a link to report
        for media_data in media_files:
            media = Media.objects.create(**media_data)
            ReportMedia.objects.create(report=report, media=media)

        return report
    
    def get_attached_media(self, obj):
        report_media = ReportMedia.objects.filter(report=obj)
        return MediaSerializer([rm.media for rm in report_media], many=True).data



        