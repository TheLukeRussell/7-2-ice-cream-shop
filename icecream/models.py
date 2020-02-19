from django.db import models
from django.urls import reverse
import datetime

AVAILABLE = [
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Seasonal', 'Seasonal'),
    ]
BASE = [
    ('Chocolate', 'Chocolate'),
    ('Vanilla', 'Vanilla'),
]
BOOL = [
    (True, 'Yes'),
    (False, 'No')
]

class Icecream(models.Model):
    flavor = models.CharField(max_length = 50)
    base = models.CharField(max_length = 11, choices=BASE)
    available = models.CharField(max_length=9, choices=AVAILABLE)
    Featured = models.BooleanField(choices=BOOL)
    date_churned = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.flavor

    def get_absolute_url(self):
        return reverse('icecream:index')

    class Meta:
        ordering = ['flavor']
