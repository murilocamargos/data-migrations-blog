from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)

class NewAddress(models.Model):
    street_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client)
