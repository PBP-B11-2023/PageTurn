from django.shortcuts import render
from django.http import HttpResponseRedirect
from laporan_buku_rusak.forms import ProductForm
from django.urls import reverse
from laporan_buku_rusak.models import Product
from peminjaman.models import Peminjaman
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

# Create your views here.
def show_laporan(request):
    # user_borrowed_books = Peminjaman.objects.filter(user=request.user, is_returned=False).select_related('book')
    products = Product.objects.all()
    context = {
        'products': products,
        # 'user_borrowed_books': user_borrowed_books,
    }
    return render(request, "laporan_buku_rusak.html", context)

def create_laporan(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('laporan_buku_rusak:show_laporan'))

    context = {'form': form}
    return render(request, "create_laporan.html", context)

def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))


@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, description=description)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()