from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    # Agrego estos campos para evitar el conflicto con AbstractUser
    groups = None
    user_permissions = None

    def __str__(self):
        return self.username
