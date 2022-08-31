from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    # id = models.AutoField(primary_key=True) #If we put AutoField then the field(like id in this line) can't be unique
    name=models.CharField(max_length=255)
    roll=models.IntegerField(unique=True)
    city=models.CharField(max_length=255)