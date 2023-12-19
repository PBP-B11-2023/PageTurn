from django.contrib import admin
from django.urls import include, path

from peminjaman.views import *

app_name = 'peminjaman'

urlpatterns = [
    path("", show_peminjaman, name="show_peminjaman"),
    path('new/', add_peminjaman, name='add_peminjaman'),
    path('history/', show_history, name='show_history'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('get-item-returned/', get_item_json_returned, name='get_item_json_returned'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('return-book/<int:id>/', return_book, name='return_book'),
    path('add-book/<int:id>/', add_book, name='add_book'),
    path('get-selected/', get_selected_books, name='get_selected_books'),
    path('get-items/', get_items_filter, name='get_items_filter'),
    path('return-book-flutter/<int:id>/', return_book_flutter, name='return_book_flutter'),
    path('get-history/', get_history, name='get_history'),
]