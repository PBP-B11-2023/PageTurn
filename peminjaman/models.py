from django.db import models

from katalog.models import Book
from PageTurn import settings


# Create your models here.
class Peminjaman(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    tgl_dipinjam = models.DateField(null=True)
    durasi_peminjaman = models.IntegerField(null=True)
    tgl_batas = models.DateField(null=True)
    tgl_dikembalikan = models.DateField(null=True)
    is_returned = models.BooleanField(default=False)
