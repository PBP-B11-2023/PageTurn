from django.contrib import admin
from django.urls import include, path

from katalog.views import *

app_name = "katalog"

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('create-book-ajax/', add_book_ajax, name='add_book_ajax'),
    path('get-book-genre/<str:genre>/', get_book_json_genre, name='get_book_json_genre'),
]