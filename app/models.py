from django.db import models

# Create your models here.

class abc(models.Model):
    name = models.CharField(max_length=20)
    age=models.CharField(max_length=50)
