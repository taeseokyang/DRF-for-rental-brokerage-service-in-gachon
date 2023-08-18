from rest_framework import serializers
from users.serializers import ProfileSerializer
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ("pk","profile", "title", "category", "body", "location","deadline_date","return_date","published_date", "done")

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "location", "deadline_date","return_date")