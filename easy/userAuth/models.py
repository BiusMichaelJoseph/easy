from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Assuming a maximum length of 15 characters
    is_verified = models.BooleanField(default=False)
 
    def __str__(self):
        return self.username