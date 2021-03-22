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
  ('SF_','https://apexassembly.com/wp-content/uploads/2019/03/San-Francisco-Golden-Gate-Bridge.jpg'),
  ('LND', 'https://imageproxy.themaven.net//https%3A%2F%2Fwww.history.com%2F.image%2FMTYyNDg1MjE3MTI1Mjc5Mzk4%2Ftopic-london-gettyimages-760251843-promo.jpg'),
  ('GBR', 'https://rccl-h.assetsadobe.com/is/image/content/dam/royal/data/ports/gibraltar-united-kingdom/overview/gibraltar-united-kingdom-view-from-beach.jpg?$750x320$')
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
  def save(self, *args, **kwargs) :
    print("+==================================================+ I'm saving!!")
    super(Post,self).save(*args, **kwargs)
  

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
  def save(self, *args, **kwargs):
    for i,a in enumerate(IMG_URLS):
      if self.city_name in a:
        self.description = a[1]
    super(City,self).save(*args, **kwargs)
  def __str__(self):
    return self.get_city_name_display()
  