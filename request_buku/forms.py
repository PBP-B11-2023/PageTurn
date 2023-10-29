from django.forms import ModelForm
from request_buku.models import Request

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ["title", "author", "description"]