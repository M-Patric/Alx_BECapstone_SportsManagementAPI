# achievements/admin.py
from django.contrib import admin
from .models import Achievement

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "athlete", "achieved_date")
    search_fields = ("title", "athlete__user__username")
