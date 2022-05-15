from django.db import models

class jobs(models.Model):
    job_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    job_dec = models.TextField()
    expo = models.IntegerField()

