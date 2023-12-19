from django.urls import path
from laporan_buku_rusak.views import show_laporan, get_product_json, add_product_ajax, show_json, create_product_flutter


# from laporan_buku_rusak.views import (add_product_ajax, get_product_json,
#                                       show_laporan)

app_name = 'laporan_buku_rusak'

urlpatterns = [
    path('', show_laporan, name='show_laporan'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('json/', show_json, name='show_json'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    # path('filter_products/', filter_products, name='filter_products'),
]