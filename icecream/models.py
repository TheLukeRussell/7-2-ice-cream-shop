from django.db import models

class Icecream(models.Model):
    flavor = models.CharField(max_length = 50)

    def __str__(self):
        return self.flavor
