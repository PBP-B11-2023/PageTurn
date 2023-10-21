from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class AdminUser(AbstractBaseUser):
    username = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
