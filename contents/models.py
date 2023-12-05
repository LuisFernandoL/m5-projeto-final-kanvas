from django.db import models
from uuid import uuid4


class Content(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    video_url = models.CharField(max_length=200, blank=True)

    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="contents"
    )
