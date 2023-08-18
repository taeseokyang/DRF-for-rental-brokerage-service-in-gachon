from rest_framework import serializers
from .models import CouncilPost

class CouncilPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouncilPost
        fields = ("pk","council", "title", "category", "location","remaining_cnt")

class CouncilPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouncilPost
        fields = ("council", "title", "category", "location")