# training/admin.py
from django.contrib import admin
from .models import TrainingSession, PerformanceRecord

@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ("athlete", "coach", "session_date", "duration_minutes")
    search_fields = ("athlete__user__username", "coach__user__username", "focus_area")

@admin.register(PerformanceRecord)
class PerformanceRecordAdmin(admin.ModelAdmin):
    list_display = ("athlete", "event_name", "date", "score", "ranking")
    search_fields = ("athlete__user__username", "event_name")
