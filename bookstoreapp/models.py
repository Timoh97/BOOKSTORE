from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

# Create your models here.
class Books(models.Model):
   file = models.FileField(upload_to='documents/')
   image = models.ImageField(upload_to='images/')
   author = models.CharField(default='Author name..',max_length=100)
   year_published = models.IntegerField(blank=True, null=True)
   title = models.CharField(default='Title of the book',max_length=100)
   price = models.IntegerField(blank=True, null=True,default='Price in dollars..')
# The profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(max_length=400, blank=True)
    name = models.CharField(blank=True, max_length=120)
    profile_pic = models.ImageField(upload_to='images/')
from django.contrib.auth.models import AbstractUser

#create custoclass User(AbstractUser):
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
