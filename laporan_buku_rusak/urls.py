from django.urls import path

from laporan_buku_rusak.views import *

app_name = 'laporan_buku_rusak'

urlpatterns = [
    path('', show_laporan, name='show_laporan'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('add-laporan/', add_laporan_flutter, name='add_laporan_flutter'),
    path('get-laporan/', get_laporan, name='get_laporan'),
]