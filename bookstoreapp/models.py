from django.db import models
from django.contrib.auth.models import AbstractUser

#create custoclass User(AbstractUser):
class User(AbstractUser):
    is_normal_user = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
