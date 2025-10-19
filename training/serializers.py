# training/serializers.py
from rest_framework import serializers
from .models import TrainingSession, PerformanceRecord
from profiles.models import AthleteProfile  # import athlete model


class TrainingSessionSerializer(serializers.ModelSerializer):
    athlete = serializers.PrimaryKeyRelatedField(queryset=AthleteProfile.objects.all())

    class Meta:
        model = TrainingSession
        fields = "__all__"


class PerformanceRecordSerializer(serializers.ModelSerializer):
    athlete = serializers.PrimaryKeyRelatedField(queryset=AthleteProfile.objects.all())

    class Meta:
        model = PerformanceRecord
        fields = "__all__"
