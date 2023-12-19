from django.contrib import admin
from django.urls import include, path

from katalog.views import *

app_name = "katalog"

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('create-book-ajax/', add_book_ajax, name='add_book_ajax'),
    path('get-genres/', get_genre_json, name='get_genre_json'),
    path('get-books-genre/', get_books_by_genre, name='get-books-by-genre'),
    path('create-flutter/', create_flutter, name='create_flutter'),
]