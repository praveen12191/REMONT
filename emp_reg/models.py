from django.db import models
class employer_details(models.Model):
    username = models.CharField(max_length=100) 
    email = models.CharField(max_length=100) 
    phone = models.CharField(max_length=50)
    password1 = models.CharField(max_length=60)
    password2 = models.CharField(max_length=60)
    
    
