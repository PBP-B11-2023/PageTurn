from django.shortcuts import render
from request_buku.models import Request
from django.http import HttpResponseRedirect, HttpResponse
from request_buku.forms import RequestForm
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

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
        user = request.user

        new_request = Request(title=title, author=author, description=description, user=user)
        new_request.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()