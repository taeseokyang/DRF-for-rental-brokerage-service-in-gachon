from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
from posts.models import Post
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    postid =  models.IntegerField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    text = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)