import datetime

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


def show_homepage(request):
    context = {}
    return render(request, "homepage.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('homepage:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admins = {"admin1" : "PWadmin1"}
        if username in admins:
            if password == admins[username]:
                user = AdminUser.objects.get(username=username)
                print(isinstance(user, AdminUser))
                login(request, user)
                response = HttpResponseRedirect(reverse("homepage:show_homepage")) 
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            user = authenticate(request, username=username, password=password)
            print(isinstance(user, AdminUser))
            if user is not None:
                login(request, user) # melakukan login terlebih dahulu
                response = HttpResponseRedirect(reverse("homepage:show_homepage")) 
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)