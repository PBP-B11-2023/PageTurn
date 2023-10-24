from django.urls import include, path
from django.contrib import admin
from katalog.views import get_books


app_name = "katalog"

urlpatterns = [
    path("",get_books, name="get_books")
]