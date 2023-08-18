from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CouncilPost(models.Model):
    council_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='council_posts')
    council = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    # likes = models.ManyToManyField(User, related_name="like_posts",blank=True)
    location = models.CharField(max_length=128, default="가천대학교")
    remaining_cnt = models.IntegerField(default=0)