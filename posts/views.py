from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from users.models import Profile
from .permissions import CustomReadOnly
from .serializers import PostSerializer, PostCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [CustomReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author','location']
    def get_serializer_class(self):
        if self.action == 'list' or 'restive':
            return PostSerializer
        return PostCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        #빌리는 카운트
        # profile.borrow_cnt+=1
        # profile.save()

        # profile.update(borrow_cnt=3)
        serializer.save(
            author=self.request.user,
            profile=profile
        )