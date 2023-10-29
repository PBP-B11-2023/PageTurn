from django.urls import path

from laporan_buku_rusak.views import (add_product_ajax, filter_products,
                                      get_product_json, show_laporan)

app_name = 'laporan_buku_rusak'

urlpatterns = [
    path('', show_laporan, name='show_laporan'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('filter_products/', filter_products, name='filter_products'),
]