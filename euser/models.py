from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

from django.db.models.deletion import CASCADE

# Create your models here.
class profile(models.Model):#one user have only one profile
    user = models.OneToOneField(User,on_delete=models.CASCADE)#cascade mean if we delete the user it will automaticly delete the profile
    image = models.ImageField(default='default.jpg',upload_to='profile_pic')
    def __str__(self):
        return f'{self.user.username} Profile'

# class employee(models.Model):
#     user, id