from django.db import models
from adminapp.models import Course

class Login(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    role=models.IntegerField(default=1)  # 0-admin 1-user

class User(models.Model):
    loginid = models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=10)
    dob=models.DateField()
    email=models.EmailField()
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    profilepic=models.ImageField(upload_to='images')
