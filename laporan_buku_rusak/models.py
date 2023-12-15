from django.db import models

<<<<<<< HEAD
=======
from katalog.models import Book
from PageTurn import settings

>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
# Create your models here.
class Laporan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_rusak = models.BooleanField(default = False)
