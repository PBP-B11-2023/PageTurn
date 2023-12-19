import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from katalog.models import Book
from laporan_buku_rusak.forms import ProductForm
from laporan_buku_rusak.models import Laporan
from peminjaman.models import Peminjaman


def show_laporan(request):
    if request.user.is_authenticated:
        bukupinjam = Peminjaman.objects.filter(user=request.user, is_returned=False)
        context = {
            'user' : request.user,
            'bukupinjam': bukupinjam,
            'last_login' : request.COOKIES["last_login"][:-10] if "last_login" in request.COOKIES else "",
        }
        return render(request, 'laporan_buku_rusak.html', context)
    else:
        context = {
            'user' : 'tamu',
        }
        return render(request, 'tamu.html', context)

def get_product_json(request):
    product_item = Laporan.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")

        user = request.user
        new_product = Laporan(name=name, description=description, user=user, is_rusak=True)
        new_product.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


@csrf_exempt
def add_laporan_flutter(request):
    selected_books = request.POST.getlist('booklist')[0]
    judul = request.POST.getlist('judul')[0]
    deskripsi = request.POST.getlist('deskripsi')[0]
    print(judul)
    print(deskripsi)
    selected_books = json.loads(selected_books)
    if selected_books:
        for id in selected_books:
            buku = Book.objects.get(pk=id)
            Laporan.objects.create(
                user = request.user,
                book = buku,
                name = judul,
                description = deskripsi,
            )
        return JsonResponse({
            "status": True,
            "message": "Berhasil membuat laporan!"
        }, status=201)
    else:
        return JsonResponse({
                "status": False,
                "message": "Terdapat Error!"
            }, status=400)
    
def get_laporan(request):
    print('tes')
    laporans = Laporan.objects.filter(user = request.user)
    print(laporans)
    return HttpResponse(serializers.serialize('json', laporans))