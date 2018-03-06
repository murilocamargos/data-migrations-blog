from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    bought = models.IntegerField(null=True)

class Computer(models.Model):
    brand = models.CharField(max_length=255)
    bought_by = models.ForeignKey(Client, related_name='computers')
