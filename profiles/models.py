# profiles/models.py
from django.db import models
from django.contrib.auth.models import User

class AthleteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="athlete_profile")
    full_name = models.CharField(max_length=255, blank=True)
    sport_type = models.CharField(max_length=120, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    skill_level = models.CharField(max_length=50, choices=[
        ("beginner","Beginner"), ("intermediate","Intermediate"), ("advanced","Advanced"), ("pro","Pro")
    ], default="beginner")
    bio = models.TextField(blank=True)
    profile_photo = models.URLField(blank=True)  # for now use URLField; replace with ImageField if you configure media
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.sport_type or 'No sport'}"

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="coach_profile")
    sport_specialty = models.CharField(max_length=120, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    certifications = models.TextField(blank=True)

    def __str__(self):
        return f"Coach {self.user.username}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="agent_profile")
    agency_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Agent {self.user.username}"

