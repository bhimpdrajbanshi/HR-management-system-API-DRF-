from django.contrib.auth.models import AbstractUser
from django.db import models
from setup.models import Role

class User(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email