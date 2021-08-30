from django.db import models

# Create your models here.

class Mesurment (models.Model):
    location = models.CharField(max_length=200)
    distance = models.CharField(max_length=200)
