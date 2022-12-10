from django.db import models

# Create your models here.
class Animal(models.Model):
  classification = models.CharField(max_length=50)
  species = models.CharField(max_length=50)
  common_name = models.CharField(max_length=100)
  name = models.CharField(max_length=50)

