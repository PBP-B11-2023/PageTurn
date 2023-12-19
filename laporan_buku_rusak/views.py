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
from django.urls import reverse
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


def show_json(request):
    data = Laporan.objects.filter(user=request.user)  
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Laporan.objects.create(
            user = request.user,
            name = data["name"],
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)




