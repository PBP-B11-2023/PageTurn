from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from homepage.models import CustomUser


@csrf_exempt
def login(request):
    username = request.POST['username'].strip()
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register(request):
    username = request.POST['username'].strip()
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    if CustomUser.objects.filter(username=username).exists():
        return JsonResponse({
            "status": False,
            "message": "Username sudah terdaftar."
        }, status=400)

    if password1 != password2:
        return JsonResponse({
            "status": False,
            "message": "Password dan Konfirmasi Password berbeda."
        }, status=400)
    
    user = CustomUser.objects.create_user(username=username, password=password1, role='member')
    user.save()
    return JsonResponse({
        "username": user.username,
        "status": True,
        "message": f"Berhasil membuat akun dengan username: {username}"
    }, status=201)

def get_user(request):
    res = {
        'role': request.user.role,
        'username' : request.user.username,
    }
    return JsonResponse(res)