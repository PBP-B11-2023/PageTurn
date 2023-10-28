from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from katalog.models import Book
from peminjaman.forms import PeminjamanForm
from peminjaman.models import Peminjaman


@login_required(login_url='/login')
def show_peminjaman(request):
    books = Book.objects.all()
    dipinjam = Peminjaman.objects.filter(user = request.user, is_returned = False)
    dikembalikan = Peminjaman.objects.filter(user = request.user, is_returned = True)
    genres = set()
    for book in Book.objects.all():
        genres.add(book.genre)
    context = {
        'user' : request.user,
        'books' : books,
        'dipinjam' : dipinjam,
        'dikembalikan' : dikembalikan,
        'genres' : genres,
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
        'form': PeminjamanForm(),
    }
    return render(request, 'add_peminjaman.html', context)

@login_required(login_url='/login')
def show_history(request):
    books = Book.objects.all()
    dikembalikan = Peminjaman.objects.filter(user = request.user, is_returned = True)
    genres = set()
    for book in Book.objects.all():
        genres.add(book.genre)
    context = {
        'user' : request.user,
        'books' : books,
        'dikembalikan' : dikembalikan,
        'genres' : genres,
    }

    return render(request, 'history_peminjaman.html', context)


def get_item_json(request):
    item = Peminjaman.objects.filter(user=request.user, is_returned = False)
    return HttpResponse(serializers.serialize('json', item))

def get_item_json_returned(request):
    item = Peminjaman.objects.filter(user=request.user, is_returned = True)
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
        form = PeminjamanForm(request.POST)
        if form.is_valid():
            buku = Book.objects.get(pk=id)
            new_item = Peminjaman(
                user=request.user,
                book=buku,
                tgl_dipinjam=datetime.now().date(),
                durasi_peminjaman=form.cleaned_data['durasi_peminjaman'],
                tgl_batas=datetime.now().date() + timedelta(days=form.cleaned_data['durasi_peminjaman']),
                is_returned=False
            )
            new_item.save()
            buku.is_dipinjam = True
            buku.save()
            return redirect('peminjaman:show_peminjaman')
    return HttpResponseNotFound()