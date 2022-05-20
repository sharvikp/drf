from django.db import models
from django.forms import CharField

# Create your models here.

class register(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)