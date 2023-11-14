from django.db import models

# Create your models here.
class Cadastre(models.Model):
    cadastre_number = models.CharField(max_length=12)
    latitude = models.FloatField()
    longitude = models.FloatField()
    external_response = models.CharField(max_length=5)