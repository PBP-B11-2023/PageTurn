from django.urls import include, path
from django.contrib import admin
from katalog.views import get_books, show_katalog, get_book_json, add_book_ajax


app_name = "katalog"

urlpatterns = [
    path("",get_books, name="get_books"),
    path('katalog/', show_katalog, name='show_katalog'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('create-book-ajax/', add_book_ajax, name='add_book_ajax'),
]