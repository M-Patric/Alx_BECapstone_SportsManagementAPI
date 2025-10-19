# training/models.py
from django.db import models
from django.contrib.auth.models import User
from profiles.models import AthleteProfile, Coach

class TrainingSession(models.Model):
    athlete = models.ForeignKey(AthleteProfile, on_delete=models.CASCADE, related_name="training_sessions")
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True, related_name="sessions")
    session_date = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=60)
    focus_area = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_training_sessions")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Training {self.athlete.user.username} on {self.session_date}"

class PerformanceRecord(models.Model):
    athlete = models.ForeignKey(AthleteProfile, on_delete=models.CASCADE, related_name="performance_records")
    event_name = models.CharField(max_length=255)
    score = models.FloatField(null=True, blank=True)
    ranking = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    remarks = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_performance_records")

    def __str__(self):
        return f"{self.event_name} - {self.athlete.user.username}"
