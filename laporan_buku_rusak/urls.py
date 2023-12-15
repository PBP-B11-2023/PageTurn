from django.urls import path
<<<<<<< HEAD
from laporan_buku_rusak.views import show_laporan, get_product_json, add_product_ajax, show_json

=======

from laporan_buku_rusak.views import (add_product_ajax, get_product_json,
                                      show_laporan)
>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8

app_name = 'laporan_buku_rusak'

urlpatterns = [
    path('', show_laporan, name='show_laporan'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
<<<<<<< HEAD
    path('json/', show_json, name='show_json'),
=======
>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
    # path('filter_products/', filter_products, name='filter_products'),
]