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

from homepage.models import *
from katalog.models import Book

from .forms import CustomUserCreationForm


def show_homepage(request):
    print(69)
    data = Book.objects.filter(author__icontains="Michelle Obama")
    print("please bekerja")
    return render(request, 'homepage.html', {'michelle_obama_books': data})

    return render(request, "homepage.html", context)

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

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('homepage:login'))
    response.delete_cookie('last_login')
    return response
