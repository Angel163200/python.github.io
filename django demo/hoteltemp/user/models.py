from datetime import datetime

from django.db import models

# Create your models here
from adminapp.models import Rooms


class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.IntegerField(default=1)  # admin-0 user-1


class Registration(models.Model):
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    email = models.EmailField()
    confirm = models.CharField(max_length=20)


class Feedback(models.Model):
    userid = models.ForeignKey(Login, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=500)
    date = models.DateField(default=datetime.now)


class Book(models.Model):
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE)
    roomid = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    persons = models.IntegerField()
    status = models.IntegerField()
