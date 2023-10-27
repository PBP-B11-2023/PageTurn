from django.shortcuts import render
from django.http import HttpResponseRedirect
from laporan_buku_rusak.forms import ProductForm
from django.urls import reverse
from laporan_buku_rusak.models import Product
from peminjaman.models import Peminjaman

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

