from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from katalog.models import Book

def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data))
    content_type = "application/json"

def show_katalog(request):
    book = Book.objects.all

    context = {
        'book': book,
        # 'products_count' : len(book),
    }

    return render(request, "katalog.html", context)

def get_book_json(request):
    book_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book_item))

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        author = request.POST.get("author")
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        price = request.POST.get("price")
        year = request.POST.get("year")
        genre = request.POST.get("genre")
        image = request.POST.get("image")
        description = request.POST.get("description")

        # Create a new Book object with the received data
        new_book = Book(
            name=name,
            author=author,
            rating=rating,
            review=review,
            price=price,
            year=year,
            genre=genre,
            image=image,
            description=description
        )

        # Save the new book to the database
        new_book.save()
        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()
