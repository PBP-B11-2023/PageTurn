from django.shortcuts import render
from request_buku.models import Request
from django.http import HttpResponseRedirect
from request_buku.forms import RequestForm
from django.urls import reverse

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