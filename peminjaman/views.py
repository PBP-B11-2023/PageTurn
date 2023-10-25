from django.shortcuts import render

from katalog.models import Book


def show_peminjaman(request):
    books = Book.objects.all()
    genres = set()
    for book in books:
        genres.add(book.genre)
    context = {
        'genres' : genres,
        'books' : books,
    }

    return render(request, 'tes.html', context)