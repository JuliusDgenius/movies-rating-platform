from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model that extends the default AbstractUser.
    """
    email = models.EmailField(unique=True)

    # Keep default username auth; email is unique for login flow
    REQUIRED_FIELDS = ["email"]
