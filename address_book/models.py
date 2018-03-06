from django.db import models

# Create your models here.
class Address(models.Model):
    street_name = models.CharField(max_length=255)

class Client(models.Model):
    name = models.CharField(max_length=255)
    addresses = models.ManyToManyField(Address)
