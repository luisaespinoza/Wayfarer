from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
  city = models.CharField(max_length=50)
  REQUIRED_FIELDS= ['city']

class Post(models.Model):
  title= models.CharField(max_length=50)
  content= models.TextField(max_length=250)
  author= models.ForeignKey('User', related_name='posts', on_delete=models.CASCADE)