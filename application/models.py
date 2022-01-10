from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
      return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = CloudinaryField('image')
    author = models.CharField(default='Author name..',max_length=100)
    year_published = models.IntegerField(blank=True, null=True)
    title = models.CharField(default='Title of the book',max_length=100)

    def __str__(self):
      return self.name

    @property
    def save_image(self):
          self.save()

    def delete_image(self):
        self.delete()