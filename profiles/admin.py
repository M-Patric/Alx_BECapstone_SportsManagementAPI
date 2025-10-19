# profiles/admin.py
from django.contrib import admin
from .models import AthleteProfile, Coach, Agent

@admin.register(AthleteProfile)
class AthleteProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "sport_type", "skill_level", "location")
    search_fields = ("user__username", "sport_type", "location")

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ("user", "sport_specialty", "experience_years")

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ("user", "agency_name", "region")
