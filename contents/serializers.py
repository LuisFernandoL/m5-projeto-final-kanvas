from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Content
from courses.serializers import CourseSerializer


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["id", "name", "content", "video_url"]
