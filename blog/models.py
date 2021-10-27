from django.db import models
from django.contrib.auth.models import User

# Models


class Notes(models.Model):
    """
    Notes Database Structure
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.title  # Display the notes title

    class Meta:
        """
        Remove the extra s to notes in the admin panel
        """
        verbose_name = 'notes'
        verbose_name_plural = 'notes'


class Assignments(models.Model):
    """
    Assignments Database Structure
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Tasks(models.Model):
    """
    Tasks Database Structure
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)
