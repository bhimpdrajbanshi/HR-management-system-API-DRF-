from django.db import models


class Role(models.Model):

    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    role_name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.role_name