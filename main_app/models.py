from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime


TYPE = (
    ('-', '--Please select--'),
    ('Cocktail', 'Cocktail'),
    ('Wine', 'Wine'),
    ('Beer', 'Beer'),
    ('Liquor', 'Liquor'),
    ('Non-Alcoholic', 'Non-Alcoholic')
)
RATING = (
    (10, 10),
    (9, 9),
    (8, 8),
    (7, 7),
    (6, 6),
    (5, 5),
    (4, 4),
    (3, 3),
    (2, 2),
    (1, 1) 
)
class Drink(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(
        max_length=100,
        choices=TYPE,
        default=TYPE[0]
    )
    rating = models.IntegerField(
        choices=RATING,
        default=RATING[0]
    )
    description = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})

    class Meta:
        ordering = ['-create_at']
