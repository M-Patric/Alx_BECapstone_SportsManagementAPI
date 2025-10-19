# profiles/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AthleteProfile, Coach, Agent
from .serializers import AthleteProfileSerializer, AthleteProfileCreateSerializer, CoachSerializer, AgentSerializer
from core.permissions import IsOwnerOrReadOnly

class AthleteProfileViewSet(viewsets.ModelViewSet):
    queryset = AthleteProfile.objects.select_related("user").all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return AthleteProfileCreateSerializer
        return AthleteProfileSerializer

    def perform_create(self, serializer):
        # set the user field to current user (create profile for self)
        serializer.save(user=self.request.user)

class CoachViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.select_related("user").all()
    serializer_class = CoachSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.select_related("user").all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
