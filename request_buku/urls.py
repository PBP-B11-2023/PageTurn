from django.urls import path
from request_buku.views import show_request, create_request, show_request_json, get_request_json, add_request_ajax, delete_request
from django.contrib import admin

app_name = 'request_buku'

urlpatterns = [
    path('', show_request, name='show_request'),
    path('create-request', create_request, name='create_request'),
    path('show_request_json/', show_request_json, name='show_request_json'),
    path('get-request/', get_request_json, name='get_request_json'),
    path('create-request-ajax/', add_request_ajax, name='add_request_ajax'),
    path('delete/<int:id>', delete_request, name='delete_request'),
]