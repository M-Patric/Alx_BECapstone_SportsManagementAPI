# matches/models.py
from django.db import models
from profiles.models import Agent, AthleteProfile
from django.contrib.auth.models import User

class TalentAgentLink(models.Model):
    STATUS_CHOICES = [("pending","Pending"), ("active","Active"), ("rejected","Rejected"), ("terminated","Terminated")]

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="talent_links")
    athlete = models.ForeignKey(AthleteProfile, on_delete=models.CASCADE, related_name="agent_links")
    match_score = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_matches")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("agent", "athlete")  # prevent duplicate matching if desired

    def __str__(self):
        return f"{self.agent.user.username} ↔ {self.athlete.user.username} ({self.status})"
