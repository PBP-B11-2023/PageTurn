from django.shortcuts import render

from katalog.models import Book
from peminjaman.models import Peminjaman


def show_peminjaman(request):
    books = Book.objects.all()
    genres = set()
    peminjaman = Peminjaman.objects.filter(user = request.user)
    for book in books:
        genres.add(book.genre)
    context = {
        'user' : request.user.username,
        'genres' : genres,
        'books' : books,
        'peminjaman' : peminjaman,
    }

    return render(request, 'tes.html', context)