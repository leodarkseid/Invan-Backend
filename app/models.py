from django.db import models
from django.contrib.auth.models import AbstractUser
from app.manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=16)
    bio = models.CharField(max_length=164, null=True )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()


class Post(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=164)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="post_user")

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=)