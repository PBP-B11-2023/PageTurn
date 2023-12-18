from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from PageTurn.review.models import Product

from katalog.models import Book
from laporan_buku_rusak.forms import ProductForm
from laporan_buku_rusak.models import Laporan
from peminjaman.models import Peminjaman


@login_required(login_url='/login')
def show_laporan(request):
    if request.method == 'POST':
        rusak = request.POST.get('rusak', False)
        if rusak:
            bukupinjam = Peminjaman.objects.filter(user=request.user, is_returned=False)
            context = {
                'bukupinjam': bukupinjam,
            }
            return render(request, 'laporan_buku_rusak.html', context)
    
    bukupinjam = Peminjaman.objects.filter(user=request.user, is_returned=False)
    context = {
        'bukupinjam': bukupinjam,
    }
    return render(request, 'laporan_buku_rusak.html', context)

def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        is_rusak = request.POST.get("is_rusak")

        user = request.user
        new_product = Product(name=name, description=description, user=user, is_rusak=True)
        new_product.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def filter_products(request):
    non_rusak = request.GET.get('non-rusak')
    rusak = request.GET.get('rusak')

    products = Product.objects.all()

    if non_rusak and rusak:
        # Tampilkan semua buku
        data = [{'name': p.name, 'is_rusak': p.is_rusak} for p in products]
    elif non_rusak:
        # Tampilkan yang non-rusak
        data = [{'name': p.name, 'is_rusak': p.is_rusak} for p in products if not p.is_rusak]
    elif rusak:
        # Tampilkan yang rusak
        data = [{'name': p.name, 'is_rusak': p.is_rusak} for p in products if p.is_rusak]
    else:
        data = []

    return JsonResponse(data, safe=False)
