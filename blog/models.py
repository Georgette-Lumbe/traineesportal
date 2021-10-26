from django.db import models
from django.contrib.auth.models import User

# Models


class Notes(models.Model):
    """
    Note Database Structure
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
