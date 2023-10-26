from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from katalog.models import Book
from peminjaman.models import Peminjaman


@login_required(login_url='/login')
def show_peminjaman(request):
    books = Book.objects.all()
    dipinjam = Peminjaman.objects.filter(user = request.user, is_returned = False)
    dikembalikan = Peminjaman.objects.filter(user = request.user, is_returned = True)
    context = {
        'user' : request.user,
        'books' : books,
        'dipinjam' : dipinjam,
        'dikembalikan' : dikembalikan,
    }

    return render(request, 'peminjaman.html', context)

@login_required
def add_peminjaman(request):
    books = Book.objects.filter(is_dipinjam = False)
    kosong = Book.objects.filter(is_dipinjam = True)
    genres = set()
    for book in Book.objects.all():
        genres.add(book.genre)
    context = {
        'books' : books,
        'genres' : genres,
        'kosong' : kosong,
    }
    return render(request, 'add_peminjaman.html', context)

def get_item_json(request):
    item = Peminjaman.objects.filter(user=request.user, is_returned = False)
    return HttpResponse(serializers.serialize('json', item))

def get_book_json(request):
    item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', item))

@csrf_exempt
def return_book(request, id):
    if request.method == 'POST':
        item = Peminjaman.objects.get(pk=id)
        item.is_returned = True
        item.tgl_dikembalikan = datetime.now().date()
        item.save()
        buku = item.book
        buku.is_dipinjam = False
        buku.cnt_dipinjam += 1
        buku.save()
        return HttpResponse(b"RETURNED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def add_book(request, id):
    if request.method == 'POST':
        buku = Book.objects.get(pk=id)
        new_item = Peminjaman.objects.create(
            user = request.user,
            book = buku,
            tgl_dipinjam = datetime.now().date(),
            tgl_batas = datetime.now().date() + timedelta(weeks=2),
            is_returned = False
        )
        new_item.save()
        buku.is_dipinjam = True
        buku.save()
        return HttpResponse(b"ADDED", status=201)
    return HttpResponseNotFound()