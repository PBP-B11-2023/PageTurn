import datetime
import hashlib

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from katalog.models import Book
from django.db.models import Max
from django.http import JsonResponse
from django.db.models import F
from django.http import JsonResponse



from homepage.models import *

from .forms import CustomUserCreationForm


def get_favourite_books(request):
    # Order the books by cnt_dipinjam in descending order and select the top 5
    books_with_highest_cnt_dipinjam = Book.objects.order_by('-cnt_dipinjam')[:5]  
    # Convert the selected books to a list of dictionaries
    book_list = list(books_with_highest_cnt_dipinjam.values())
    
    return JsonResponse({'favourite_books': book_list})

def show_homepage(request):
    highest_cnt_dipinjam = Book.objects.aggregate(max_cnt_dipinjam=Max('cnt_dipinjam'))['max_cnt_dipinjam']
    books_with_highest_cnt_dipinjam = Book.objects.filter(cnt_dipinjam=highest_cnt_dipinjam)
    return render(request, 'homepage.html', {'favourite_books': books_with_highest_cnt_dipinjam})

def register(request):
    form = CustomUserCreationForm() #CustomUserCreationForm() imported from forms.py

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('homepage:show_homepage')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("homepage:show_homepage")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
