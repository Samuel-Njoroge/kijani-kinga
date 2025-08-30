from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Report, ReportMedia
from .serializers import ReportSerializer, ReportMediaSerializer


# Report ViewSet.
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def verify(self, request, pk=None):
        """Mark a report as verified"""
        report = self.get_object()
        if report.status != "pending":
            return Response({"detail": "Only pending reports can be verified"}, status=status.HTTP_400_BAD_REQUEST)
        
        report.status = "verified"
        report.save()
        return Response(ReportSerializer(report).data, status=status.HTTP_200_OK )
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def close(self, request, pk=None):
        """Close a verified report"""
        report = self.get_object()
        if report.status != "verified":
            return Response({"detail": "Only verified reports can be closed"}, status=status.HTTP_400_BAD_REQUEST)
        
        report.status = "closed"
        report.save()
        return Response(Report(report).data, status=status.HTTP_200_OK)


# Report Media ViewSet
class ReportMediaViewSet(viewsets.ModelViewSet):
    queryset = ReportMedia.objects.all()
    serializer_class = ReportMediaSerializer
    permission_classes = [permissions.IsAuthenticated]
