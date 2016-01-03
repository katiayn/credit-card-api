from django.db import models
from django.utils import timezone

class Creditcard(models.Model):
    number = models.CharField(max_length=16)
    name = models.CharField(max_length=50)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.name
