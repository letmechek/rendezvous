from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.description}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'listing_id': self.id})

    