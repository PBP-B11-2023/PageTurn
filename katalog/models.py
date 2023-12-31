from django.db import models

# Create your models here.
# Name, Author,User Rating,Reviews,Price,Year,Genre, image, description

class Book(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    rating =  models.FloatField(null=True, blank=True, default=0)
    review =   models.IntegerField(null=True, blank=True, default=0)
    price = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_dipinjam = models.BooleanField(default=False)
    cnt_dipinjam = models.IntegerField(default=0)
    