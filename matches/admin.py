# matches/admin.py
from django.contrib import admin
from .models import TalentAgentLink

@admin.register(TalentAgentLink)
class TalentAgentLinkAdmin(admin.ModelAdmin):
    list_display = ("agent", "athlete", "status", "match_score")
    search_fields = ("agent__user__username", "athlete__user__username")
