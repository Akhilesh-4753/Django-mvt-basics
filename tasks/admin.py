from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "priority", "completed", "created_at")
    list_filter = ("priority", "completed")
    search_fields = ("title", "description")
    ordering = ("-created_at",)
