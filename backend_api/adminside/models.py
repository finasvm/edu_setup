from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class education(models.Model):
    course=models.CharField(max_length=255)
    university = models.CharField(max_length=150)
    year = models.PositiveIntegerField(default=0)
    canuser = models.ForeignKey(User,on_delete=models.CASCADE)

class Userside(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)

class Eductaiondetails(models.Model):
    course=models.CharField(max_length=255)
    university = models.CharField(max_length=150)
    year = models.PositiveIntegerField(default=0)
    userdet = models.ForeignKey(Userside,on_delete=models.CASCADE)
