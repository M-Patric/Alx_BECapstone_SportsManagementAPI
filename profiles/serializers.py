# profiles/serializers.py
from rest_framework import serializers
from .models import AthleteProfile, Coach, Agent
from django.contrib.auth.models import User
from users.serializers import UserSerializer  # reuse simple user serializer if defined

class AthleteProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = AthleteProfile
        fields = ["id", "user", "full_name", "sport_type", "birth_date", "location", "skill_level", "bio", "profile_photo", "created_at", "updated_at"]

class AthleteProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteProfile
        exclude = ("created_at", "updated_at",)

class CoachSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Coach
        fields = ["id", "user", "sport_specialty", "experience_years", "certifications"]

class AgentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Agent
        fields = ["id", "user", "agency_name", "phone", "region"]
