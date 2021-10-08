from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    """Author Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)