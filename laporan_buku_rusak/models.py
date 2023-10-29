from django.db import models

from katalog.models import Book
from PageTurn import settings


# Create your models here.
class Laporan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_rusak = models.BooleanField(default = False)