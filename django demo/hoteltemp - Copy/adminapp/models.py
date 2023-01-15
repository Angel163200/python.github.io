from django.db import models


# Create your models here.

class Rooms(models.Model):
    r_image = models.ImageField(upload_to='images')
    room_no = models.IntegerField()
    floor_no = models.IntegerField()
    type = models.CharField(max_length=30)
    size = models.IntegerField()
    capacity = models.IntegerField()
    view = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    price = models.IntegerField()

