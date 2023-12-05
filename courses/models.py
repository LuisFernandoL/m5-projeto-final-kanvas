from django.db import models
from django.db.models import TextChoices
from uuid import uuid4


class CoursesStatusEnum(TextChoices):
    NS = "not started"
    IP = "in progress"
    FI = "finished"


class Course(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11, choices=CoursesStatusEnum.choices, default=CoursesStatusEnum.NS
    )
    start_date = models.DateField()
    end_date = models.DateField()

    instructor = models.ForeignKey(
        "accounts.Account", on_delete=models.PROTECT, related_name="courses", null=True
    )

    students = models.ManyToManyField(
        "accounts.Account",
        related_name="my_courses",
        through="students_courses.StudentCourse",
    )
