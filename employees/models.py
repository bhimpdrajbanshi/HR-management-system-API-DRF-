from django.db import models
from django.conf import settings

class Employee(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("suspended", "Suspended"),
    )

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee"
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="employees_created"
    )

    updated_at = models.DateTimeField(auto_now=True)

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="employees_updated",
        null=True,
        blank=True
    )
    
    is_void = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"