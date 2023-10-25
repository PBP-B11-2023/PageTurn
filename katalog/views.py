from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from katalog.models import Book


def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data),
    content_type = "application/json")
