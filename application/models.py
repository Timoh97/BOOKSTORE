from django.db import models

# Create your models here.
class Books(models.Model):
   file = models.FileField(upload_to='documents/')
   image = models.ImageField(upload_to='images/')
   author = models.TextField(default='Author name..')
   year_published = models.IntegerField(blank=True, null=True)
   title = models.TextField(default='Title of the book')
   price = models.IntegerField(blank=True, null=True,default='Price in dollars..')