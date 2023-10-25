from django.contrib.auth.models import User
from django.db import models

from katalog.models import Book


# Create your models here.
class Peminjaman:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bool = models.ForeignKey(Book, on_delete=models.CASCADE)
    tgl_dipinjam = models.DateField(null=True)
    tgl_dikembalikan = models.DateField(null=True)
