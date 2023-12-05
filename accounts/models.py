from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser



class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)
