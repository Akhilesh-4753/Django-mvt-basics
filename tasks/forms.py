from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        max_length=15,
        error_messages={
            'required': 'Title is required.',
            'max_length': 'Title cannot exceed 15 characters.',
        }
    )

    description = forms.CharField(
        required=True,
        max_length=25,
        error_messages={
            'required': 'Description is required.',
            'max_length': 'Description cannot exceed 25 characters.',
        }
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']