# matches/serializers.py
from rest_framework import serializers
from .models import TalentAgentLink

class TalentAgentLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalentAgentLink
        fields = ["id", "agent", "athlete", "match_score", "notes", "start_date", "end_date", "status", "created_by", "created_at"]
        read_only_fields = ["created_by", "created_at"]
