# training/views.py
from rest_framework import viewsets, permissions
from .models import TrainingSession, PerformanceRecord
from .serializers import TrainingSessionSerializer, PerformanceRecordSerializer
from core.permissions import IsOwnerOrReadOnly

class TrainingSessionViewSet(viewsets.ModelViewSet):
    queryset = TrainingSession.objects.select_related("athlete", "coach").all()
    serializer_class = TrainingSessionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PerformanceRecordViewSet(viewsets.ModelViewSet):
    queryset = PerformanceRecord.objects.select_related("athlete").all()
    serializer_class = PerformanceRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
