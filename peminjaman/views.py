import json
from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from katalog.models import Book
from peminjaman.forms import PeminjamanForm
from peminjaman.models import Peminjaman


def show_peminjaman(request):
    if request.user.is_authenticated:
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
            'last_login' : request.COOKIES["last_login"][:-10] if "last_login" in request.COOKIES else "",
        }

        return render(request, 'peminjaman.html', context)
    else:
        books = Book.objects.filter()
        genres = set()
        for book in Book.objects.all():
            genres.add(book.genre)
        context = {
            'books' : books,
            'genres' : genres,
        }
        return render(request, 'guest_peminjaman.html', context)

@login_required(login_url='/peminjaman')
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
        'last_login' : request.COOKIES["last_login"][:-10] if "last_login" in request.COOKIES else "",
    }
    return render(request, 'add_peminjaman.html', context)

@login_required(login_url='/peminjaman')
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
        'last_login' : request.COOKIES["last_login"][:-10] if "last_login" in request.COOKIES else "",
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
            new_item = Peminjaman.objects.create(
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
            return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def get_selected_books(request):
    selected_books = request.POST.getlist('booklist')[0]
    durasi = request.POST.getlist('durasi')[0]
    try:
        durasi = int(durasi)
        if durasi > 14 or durasi < 1:
            raise Exception()
    except:
        return JsonResponse({
                "status": False,
                "message": "Durasi hanya dapat berupa angka antara 1-14!"
            }, status=400)
    
    selected_books = json.loads(selected_books)
    if selected_books:
        for id in selected_books:
            buku = Book.objects.get(pk=id)
            new_item = Peminjaman.objects.create(
                user=request.user,
                book=buku,
                tgl_dipinjam=datetime.now().date(),
                durasi_peminjaman=durasi,
                tgl_batas=datetime.now().date() + timedelta(days=durasi),
                is_returned=False
            )
            new_item.save()
            buku.is_dipinjam = True
            buku.save()
        return JsonResponse({
            "status": True,
            "message": "Berhasil meminjam buku!"
        }, status=201)
    else:
        return JsonResponse({
                "status": False,
                "message": "Terdapat Error!"
            }, status=400)

@csrf_exempt
def return_book_flutter(request, id):
    if request.method == 'POST':
        item = Peminjaman.objects.get(pk=id)
        item.is_returned = True
        item.tgl_dikembalikan = datetime.now().date()
        item.save()
        buku = item.book
        buku.is_dipinjam = False
        buku.cnt_dipinjam += 1
        buku.save()
        if item.tgl_dikembalikan > item.tgl_batas:
            return JsonResponse({
                    "status": True,
                    "message": "Lain kali jangan telat ya mengembalikan bukunya!"
                }, status=201)
        else:
            return JsonResponse({
                    "status": True,
                    "message": "Terima kasih telah mengembalikan buku ini tepat waktu!"
                }, status=201)
    return JsonResponse({
                    "status": False,
                    "message": "Error!"
                }, status=400)


def get_items_filter(request):
    search_query = request.GET.get('search', '')
    genres = request.GET.getlist('genres')
    print('genre',genres)
    peminjamans = Peminjaman.objects.filter(user = request.user)
    item_ret = []
    
    for item in peminjamans:
        if item.is_returned:
            continue
        book = item.book
        if search_query.lower() in book.name.lower() or search_query.lower() in book.author.lower():
            if genres:
                if book.genre in genres:
                    item_ret.append(item)
            else:
                item_ret.append(item)
    
    # Serialisasi data buku ke JSON
    return HttpResponse(serializers.serialize('json', item_ret))

def get_history(request):
    search_query = request.GET.get('search', '')
    genres = request.GET.getlist('genres')
    print('genre',genres)
    peminjamans = Peminjaman.objects.filter(user = request.user)
    item_ret = []
    
    for item in peminjamans:
        if not item.is_returned:
            continue
        book = item.book
        if search_query.lower() in book.name.lower() or search_query.lower() in book.author.lower():
            if genres:
                if book.genre in genres:
                    item_ret.append(item)
            else:
                item_ret.append(item)
    
    # Serialisasi data buku ke JSON
    return HttpResponse(serializers.serialize('json', item_ret))
