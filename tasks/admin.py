from django.contrib import admin
from .models import Task, Contact

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "priority", "completed", "created_at")
    list_filter = ("priority", "completed")
    search_fields = ("title", "description")
    ordering = ("-created_at",)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone")
    search_fields = ("name", "phone")