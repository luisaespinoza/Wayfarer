from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
  city = models.CharField(max_length=50)
  REQUIRED_FIELDS= ['city']