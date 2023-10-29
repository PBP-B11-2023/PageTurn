from django.shortcuts import render
from django.http import HttpResponseRedirect
from review.forms import ProductForm
from django.urls import reverse
from review.models import Review
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.views.decorators.csrf import csrf_exempt

def show_main(request):
    reviews = Review.objects.all()

    context = {
        'name': 'Pak Bepe', # Nama kamu
        'pesan': 'PBP A', # Kelas PBP kamu
        'review': reviews
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
    # Get review berdasarkan ID
    review = Review.objects.get(pk = id)

    # Set review sebagai instance dari form
    form = ProductForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('review_buku:show_main'))

    context = {'form': form}
    return render(request, "edit_review.html", context)

def delete_review(request, id):
    # Get data berdasarkan ID
    review = Review.objects.get(pk = id)
    # Hapus data
    review.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('review_buku:show_main'))

def get_review_json(request):
    review_item = Review.objects.all()
    return HttpResponse(serializers.serialize('json', review_item))

@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")

        new_review = Review(name=name, description=description,)
        new_review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()





# Create your views here.
