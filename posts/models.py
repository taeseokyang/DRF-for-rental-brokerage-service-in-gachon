from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField()

    done = models.BooleanField(default=False)
    # likes = models.ManyToManyField(User, related_name="like_posts",blank=True)
    location = models.CharField(max_length=128, default="가천대학교")
    deadline_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)