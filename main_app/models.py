from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    rating = models.IntegerField()
    price  = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})
