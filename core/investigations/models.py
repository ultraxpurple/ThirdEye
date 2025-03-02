# investigations/models.py
from django.db import models
from django.contrib.auth.models import User

class Investigation(models.Model):
    investigation_name = models.CharField(
        max_length=255,
        default='Untitled Investigation',  # Default value added
        help_text="Enter the name or title of the investigation."
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('COMPLETED', 'Completed'),
            ('FAILED', 'Failed'),
        ],
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    execution_logs = models.TextField(blank=True, null=True)
    report_loc = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.investigation_name} (Status: {self.status})"
