from django.urls import path
from laporan_buku_rusak.views import show_laporan, create_laporan 

app_name = 'laporan_buku_rusak'

urlpatterns = [
    path('', show_laporan, name='show_laporan'),
    path('create-laporan', create_laporan, name='create_laporan'),
]