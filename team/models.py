from django.db import models
from datetime import datetime

# Create your models here.
class Players(models.Model):
    name = models.CharField(max_length=50) 
    profile_pic = models.ImageField(upload_to='photos/%Y/%m/%d/',default='default.png')
    position = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name 
