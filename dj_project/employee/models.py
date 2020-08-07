from django.db import models

class Employee(models.Model):
  name=models.CharField(max_length=40)
  designation=models.CharField(max_length=100)
# Create your models here.
