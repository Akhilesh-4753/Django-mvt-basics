from django.db import models

class Task(models.Model):
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name