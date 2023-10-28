from django.urls import path
from laporan_buku_rusak.views import show_laporan, create_laporan, get_product_json, add_product_ajax

app_name = 'laporan_buku_rusak'

urlpatterns = [
    path('', show_laporan, name='show_laporan'),
    path('create-laporan', create_laporan, name='create_laporan'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
]