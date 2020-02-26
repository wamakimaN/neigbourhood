from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
  name = models.TextField(max_length = 100, blank = True)
  health = models.TextField(max_length = 200)
  police = models.TextField(max_length = 200)
  
class Business(models.Model):
  neighbor = models.ForeignKey(Neighborhood, null = True, blank = True)
  name = models.TextField(max_length = 100, blank = True)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  bio = models.TextField(max_length = 100, blank = True)
  profile_pic = models.ImageField(default= 'default.jpg', upload_to='profile_pics')
  business = models.ForeignKey(Business, null = True, blank = True)
  
  def __str__(self):
    return f'{self.user.username} Profile'

class Post(models.Model):
  profile = models.ForeignKey(Profile, null = True, blank = True)
  image = models.ImageField(upload_to='post_pics')
  posted_on = models.DateTimeField(auto_now_add=True,null = True)
  body = models.TextField(max_length = 200)


  



