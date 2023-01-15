from django.db import models

# Create your models here.
class Course(models.Model):
    coursename = models.CharField(max_length=10)
