# matches/views.py
from rest_framework import viewsets, permissions
from .models import TalentAgentLink
from .serializers import TalentAgentLinkSerializer
from core.permissions import IsOwnerOrReadOnly

class TalentAgentLinkViewSet(viewsets.ModelViewSet):
    queryset = TalentAgentLink.objects.select_related("agent__user", "athlete__user").all()
    serializer_class = TalentAgentLinkSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
