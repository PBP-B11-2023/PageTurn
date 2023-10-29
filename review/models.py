from django.db import models
from katalog.models import Book
from PageTurn import settings


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()
# Create your models here.
