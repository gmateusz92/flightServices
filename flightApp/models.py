from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth import get_user_model

class Flight(models.Model):
    flightNumber = models.CharField(max_length = 10)
    operatingAirlines = models.CharField(max_length=10)
    departureCity = models.CharField(max_length=20, blank=True, null=True)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estitmatedTimeOfDeparture = models.TimeField()

class Passenger(models.Model):
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 20) 
    middleName = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 10)

class Reservation(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

@receiver(post_save, sender=get_user_model())
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)  