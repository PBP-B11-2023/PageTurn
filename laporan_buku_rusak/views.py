from django.shortcuts import render
from django.http import HttpResponseRedirect
from katalog.models import Book
from laporan_buku_rusak.forms import ProductForm
from django.urls import reverse
from laporan_buku_rusak.models import Product
from peminjaman.models import Peminjaman
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url='/login')
def show_laporan(request):
    bukupinjam = Peminjaman.objects.filter(user=request.user, is_returned=False)
    context = {
        'user' : request.user,
        'bukupinjam': bukupinjam,
        'last_login' : request.COOKIES["last_login"][:-10] if "last_login" in request.COOKIES else "",
    }
    return render(request, 'laporan_buku_rusak.html', context)

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")

        user = request.user
        new_product = Product(name=name, description=description, user=user, is_rusak=True)
        new_product.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()



