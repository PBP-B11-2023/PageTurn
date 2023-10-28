from django.shortcuts import render
from django.http import HttpResponseRedirect
from review.forms import ProductForm
from django.urls import reverse
from review.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.views.decorators.csrf import csrf_exempt

def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Pak Bepe', # Nama kamu
        'pesan': 'PBP A', # Kelas PBP kamu
        'products': products
    }

    return render(request, "reviewbuku.html", context)

def create_review(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('review_buku:show_main'))
        # review = form.save(commit=False)
        # review.user = request.user
        # review.save()
        # return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_review.html", context)

def edit_review(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('review_buku:show_main'))

    context = {'form': form}
    return render(request, "edit_review.html", context)

def delete_review(request, id):
    # Get data berdasarkan ID
    product = Product.objects.get(pk = id)
    # Hapus data
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('review_buku:show_main'))

def get_review_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")

        new_product = Product(name=name, description=description,)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()





# Create your views here.
