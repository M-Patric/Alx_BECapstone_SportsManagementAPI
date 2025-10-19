# achievements/views.py
from rest_framework import viewsets, permissions
from .models import Achievement
from .serializers import AchievementSerializer
from core.permissions import IsOwnerOrReadOnly

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.select_related("athlete__user").all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
