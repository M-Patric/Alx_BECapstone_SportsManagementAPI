# achievements/models.py
from django.db import models
from profiles.models import AthleteProfile

class Achievement(models.Model):
    athlete = models.ForeignKey(AthleteProfile, on_delete=models.CASCADE, related_name="achievements")
    title = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255, blank=True)
    achieved_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    media_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.athlete.user.username}"
