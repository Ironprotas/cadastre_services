from django.db import models


class CadastreRequest(models.Model):
    cadastre_number = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    external_response = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.cadastre_number} - {self.external_response}"

