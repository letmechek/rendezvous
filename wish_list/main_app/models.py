from django.db import models

# Create your models here.
class Wishlist(models.Model):
  description = models.CharField(max_length=250)
  