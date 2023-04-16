from django.db import models
from django.contrib.auth.models import AbstractUser
from app.manager import UserManager


def User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(defaultTrue)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    objects = UserManager
