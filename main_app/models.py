from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TYPE = (
    ('-', '--Please select--'),
    ('Cocktail', 'Cocktail'),
    ('Wine', 'Wine'),
    ('Beer', 'Beer'),
    ('Liquor', 'Liquor'),
    ('Non-Alcoholic', 'Non-Alcoholic')
)

class Drink(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=100,
        choices=TYPE,
        default=TYPE[0]
    )
    description = models.TextField(max_length=500)
    rating = models.IntegerField()
    price  = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})

    class Meta:
        ordering = ['-rating']
