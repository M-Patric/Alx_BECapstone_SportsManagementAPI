# achievements/serializers.py
from rest_framework import serializers
from .models import Achievement

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ["id", "athlete", "title", "event_name", "achieved_date", "description", "media_url", "created_at"]
        read_only_fields = ["created_at"]
