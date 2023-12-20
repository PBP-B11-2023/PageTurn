import json

from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

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

def get_books_by_genre(request):
    search_query = request.GET.get('search', '')
    genres = request.GET.getlist('genres')
    if genres:
        books = Book.objects.filter(genre__in=genres)
    else:
        books = Book.objects.all()
    books_ret = []
    for book in books:
        if search_query.lower() in book.name.lower() or search_query.lower() in book.author.lower():
            books_ret.append(book)
    # Serialisasi data buku ke JSON
    return HttpResponse(serializers.serialize('json', books_ret))

def get_genre_json(request):
    book_item = Book.objects.all()
    tmp = set()
    for x in book_item:
        tmp.add(x.genre)
    genres = []
    for x in tmp:
        genres.append(x)
    return JsonResponse({'genres': genres})

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

@csrf_exempt
def create_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Book.objects.create(
            name=data['name'],
            author=data['author'],
            year=data['year'],
            rating=data['rating'],
            review=data['review'],
            price=data['price'],
            genre=data['genre'],
            image=data['image'],
            description=data['description'],
            is_dipinjam = False,
            cnt_dipinjam = 0,
        )
        return JsonResponse({"status": "success"}, status=200)
    return JsonResponse({"status": "error"}, status=401)