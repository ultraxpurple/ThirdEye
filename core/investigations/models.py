from django.db import models
from django.contrib.auth.models import User  # Using Django’s default User model

class Investigation(models.Model):
    # Django automatically creates an auto-increment PK named 'id' by default.
    # If you specifically want 'investigation_id' as the PK, you can do so, 
    # but it's optional. We'll stick with the Django default "id".

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
        return f"Investigation #{self.id} - Status: {self.status}"
