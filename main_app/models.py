from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.
CITIES = (
  ('SF_', 'San Francisco' ),
  ('LND', 'London' ),
  ('GBR', 'Gibraltar')
)
IMG_URLS = (
  ('SF_','San Francisco image URL here.'),
  ('LND', 'London image URL here.'),
  ('GBR', 'Gibralter image URL here.')
)

class User(AbstractUser):
  city = models.CharField(max_length=50)
  REQUIRED_FIELDS= ['city']

class Post(models.Model):
  title= models.CharField(max_length=50)
  content= models.TextField(max_length=250)
  author= models.ForeignKey('User', related_name='posts',on_delete=models.CASCADE)
  city = models.ForeignKey('City', related_name='posts',on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

class City(models.Model):
  city_name = models.CharField(
    max_length=3,
    choices=CITIES,
    default=CITIES[0][0]
  )
  city_photo_url = models.CharField(
    max_length=3,
    choices=IMG_URLS,
    default=IMG_URLS[0][0]
    )
  def save():
    for i,a in enumerate(IMG_URLS):
      if self.name in a:
        self.description = a[1]
    super(City,self).save(*args, **kwargs)
  def __str__(self):
    return self.get_city_name_display()
  