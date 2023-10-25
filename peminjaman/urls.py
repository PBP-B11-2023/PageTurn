from django.contrib import admin
from django.urls import include, path

from peminjaman.views import *

app_name = 'peminjaman'

urlpatterns = [
    path("", show_peminjaman, name="show_peminjaman")
]