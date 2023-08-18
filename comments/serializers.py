from rest_framework import serializers
from users.serializers import ProfileSerializer
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ("pk","postid","profile","text","created_date")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("postid", "text")