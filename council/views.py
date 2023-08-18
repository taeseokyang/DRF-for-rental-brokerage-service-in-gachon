from django.shortcuts import render
from rest_framework import viewsets
from .models import CouncilPost
from .permissions import CustomReadOnly
from .serializers import CouncilPostSerializer, CouncilPostCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CouncilPostViewSet(viewsets.ModelViewSet):
    queryset = CouncilPost.objects.all()
    permission_classes = [CustomReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['council']
    def get_serializer_class(self):
        if self.action == 'list' or 'restive':
            return CouncilPostSerializer
        return CouncilPostCreateSerializer

    def perform_create(self, serializer):


        serializer.save(
            council_user=self.request.user,
        )