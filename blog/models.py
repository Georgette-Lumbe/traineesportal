"""Modules"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Models

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Post database structure
    """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    objects = models.Manager()

    def __str__(self):
        return str(self.title)

    class Meta:
        """
        Order  our posts on the created_on field
        using descending order
        """
        ordering = ["-created_on"]


class Comment(models.Model):
    """
    Comment database structure
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=90)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    class Meta:
        """
        Order  our posts on the created_on field
        """
        ordering = ["created_on"]


class Notes(models.Model):
    """
    Notes Database Structure
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return str(self.title)  # Display the notes title

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

    def __str__(self):  # Display the assignments title
        return str(self.title)

    class Meta:
        """
        Remove the extra s to assignments in the admin panel
        """
        verbose_name = 'assignments'
        verbose_name_plural = 'assignments'


class Tasks(models.Model):
    """
    Tasks Database Structure
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)
    objects = models.Manager()  # Object member

    def __str__(self):      # Display the tasks title
        return str(self.title)

    class Meta:
        """
        Remove the extra s to tasks in the admin panel
        """
        verbose_name = 'tasks'
        verbose_name_plural = 'tasks'
