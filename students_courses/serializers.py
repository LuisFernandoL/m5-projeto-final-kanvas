from rest_framework import serializers
from accounts.models import Account
from courses.models import Course
from .models import StudentCourse


class StudentInCourseSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(source="student.id", read_only=True)
    student_username = serializers.CharField(source="student.username", read_only=True)
    student_email = serializers.CharField(source="student.email")

    class Meta:
        model = StudentCourse
        fields = ["id", "student_id", "student_username", "student_email", "status"]
        read_only_fields = ["id", "status"]


class CourseStudentSerializer(serializers.ModelSerializer):
    students_courses = StudentInCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        read_only_fields = ["id", "name"]

    def update(self, instance, validated_data):
        students_exists = []
        students_not_exists = []

        for student_course in validated_data["students_courses"]:
            student = student_course["student"]
            student_found = Account.objects.filter(email=student["email"]).first()
            if not student_found:
                students_not_exists.append(student["email"])
            else:
                students_exists.append(student_found)
        if len(students_not_exists):
            message = ", ".join(students_not_exists)
            raise serializers.ValidationError(
                {"detail": f"No active accounts was found: {message}."}
            )
        if not self.partial:
            instance.students.add(*students_exists)
            instance.save()
        return instance
