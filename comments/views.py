from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment
from users.models import Profile
from posts.models import Post
from comments.models import Comment
from .permissions import CustomReadOnly, PostWriter
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
        post = Post.objects.get(pk=self.request.data['postid'])
        serializer.save(
            writer=self.request.user,
            post = post,
            profile = profile
        )

class BorrowDone(APIView):
    def get(self, request,writer,commentid):
        #게시글 제작자의 borrow 증가
        comment_user = Profile.objects.get(user=writer)
        borrow_user = Profile.objects.get(user=request.user)
        comment = Comment.objects.get(pk=commentid)
        if comment.post.author==request.user:
            comment_user.lend_cnt += 1
            borrow_user.borrow_cnt+=1
            comment_user.save()
            borrow_user.save()
            return Response("done")
        return Response("nope")
        #수락 당한 사람의 lend 증가



