from django.db import models
from django.urls import reverse

class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    rating = models.IntegerField()
    price  = models.CharField(max_length=5)

    def __str__(self):
        return self.name
    
    