from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Course
from accounts.serializers import AccountSerializer
from students_courses.models import StudentCourse
from accounts.models import Account


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "contents": {"read_only": True},
            "students_courses": {"read_only": True},
        }


