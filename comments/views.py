from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment
from users.models import Profile
from posts.models import Post
from .permissions import CustomReadOnly
from .serializers import CommentSerializer, CommentCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [CustomReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post','writer']
    def get_serializer_class(self):
        if self.action == 'list' or 'restive':
            return CommentSerializer
        return CommentCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        post = Post.objects.get(pk=self.request.POST.get("postid", default=1))

        serializer.save(
            writer=self.request.user,
            post = post,
            profile = profile
        )