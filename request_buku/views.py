import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from request_buku.forms import RequestForm
from request_buku.models import Request


# Create your views here.
def show_request(request):
    requests = Request.objects.all()
    context = {
        'requests': requests
    }

    return render(request, "request_buku.html", context)

def create_request(request):
    form = RequestForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('request_buku:show_request'))

    context = {'form': form}
    return render(request, "create_request.html", context)

def show_request_json(request):
    data = Request.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_request_json(request):
    request_item = Request.objects.all()
    return HttpResponse(serializers.serialize('json', request_item))

@csrf_exempt
def add_request_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")

        new_request = Request(title=title, author=author, description=description)
        new_request.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_request(request, id):
    request = Request.objects.get(pk = id)
    request.delete()
    return HttpResponseRedirect(reverse('request_buku:show_request'))

@csrf_exempt
def create_request_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_request = Request.objects.create(
            user = request.user,
            title = data["title"],
            author = data["author"],
            description = data["description"]
        )

        new_request.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)