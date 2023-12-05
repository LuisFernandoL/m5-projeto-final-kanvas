from django.db import models
from django.db.models import TextChoices
from uuid import uuid4


class StudentCourseStatusEnum(TextChoices):
    PE = "pending"
    AC = "accepted"


# Create your models here.
class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    status = models.CharField(
        choices=StudentCourseStatusEnum.choices, default=StudentCourseStatusEnum.PE
    )
    student = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="students_courses",
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="students_courses",
    )
