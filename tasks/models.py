from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = (
        ("Incomplete", "Incomplete"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed")
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField(default=timezone.now)    # Set the default value of due_date to the current date and time.
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Incomplete")

    def __str__(self):
        return self.title
