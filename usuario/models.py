from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    valid_email = models.BooleanField(default=None)
    confirmation_code = models.CharField(max_length=8)
