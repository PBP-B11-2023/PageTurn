from django.forms import ModelForm
from laporan_buku_rusak.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description"]