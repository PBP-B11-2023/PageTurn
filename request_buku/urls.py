from django.urls import path
from request_buku.views import show_request, create_request
from django.contrib import admin

app_name = 'request_buku'

urlpatterns = [
    path('', show_request, name='show_request'),
    path('create-request', create_request, name='create_request'),
]