from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomRoles(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Male')
    can_view_both = models.BooleanField(default=False)

    def __str__(self):
        return self.username
