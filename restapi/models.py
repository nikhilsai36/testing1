from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    country = models.CharField(max_length=30)


class Group(models.Model):
    Branch = models.CharField(max_length=30)

