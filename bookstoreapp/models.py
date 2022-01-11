from django.db import models

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