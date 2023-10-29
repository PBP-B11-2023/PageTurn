from django.db import models
from PageTurn import settings
from katalog.models import Book


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_rusak = models.BooleanField(default = False)