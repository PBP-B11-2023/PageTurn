from django.contrib import admin
from django.urls import include, path

from katalog.views import add_book_ajax, get_book_json, get_books, show_katalog

app_name = "katalog"

urlpatterns = [
    path("",get_books, name="get_books"),
    path('katalog/', show_katalog, name='show_katalog'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('create-book-ajax/', add_book_ajax, name='add_book_ajax'),
]