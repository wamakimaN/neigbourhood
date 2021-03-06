from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
  name = models.CharField(max_length = 100, blank = True)
  health = models.CharField(max_length = 200)
  police = models.CharField(max_length = 200)
  
  def __str__(self):
    return f'{self.name}'

class Business(models.Model):
  neighbor = models.ForeignKey(Neighborhood, null = True, blank = True)
  name = models.TextField(max_length = 100, blank = True)

class Profile(models.Model):
  neighbor = models.ForeignKey(Neighborhood, null = True, blank = True)
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  bio = models.TextField(max_length = 100, blank = True)
  profile_pic = models.ImageField(default= 'default.jpg', upload_to='profile_pics')
  
  def __str__(self):
    return f'{self.user.username} Profile'

class Post(models.Model):
  neighbor = models.ForeignKey(Neighborhood, null = True, blank = True)
  profile = models.ForeignKey(Profile, null = True, blank = True)
  image = models.ImageField(upload_to='post_pics',null = True,blank = True)
  posted_on = models.DateTimeField(auto_now_add=True,null = True)
  body = models.TextField(max_length = 200)


  



