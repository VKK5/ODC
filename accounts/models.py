from django.db import models
from django.contrib.auth.models import AbstractUser
from django_google_maps import fields as map_fields
# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)
    city      =  models.CharField(max_length=100)
    state      =  models.CharField(max_length=100)
    address      =  models.CharField(max_length=100)


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = map_fields.AddressField(max_length=200)
    
    geolocation = map_fields.GeoLocationField(max_length=100)

