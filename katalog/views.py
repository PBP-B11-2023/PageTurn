from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from katalog.models import Book

from .forms import BookForm


def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data),
    content_type = "application/json")

def show_katalog(request):
    book = Book.objects.all()
    
    context = {
        'book': book,
    }

    return render(request, "katalog.html", context)

def get_book_json(request):
    book_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book_item))

def get_book_json_genre(request, genre):
    print(request.user.username)
    book_item = Book.objects.filter(genre = genre)
    return HttpResponse(serializers.serialize('json', book_item))

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "CREATED"}, status=201)
        else:
            return JsonResponse({"status": "error", "FORM NOT VALID": form.errors}, status=400)
    return JsonResponse({"status": "error"}, status=400)
