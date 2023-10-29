from django.forms import ModelForm

from laporan_buku_rusak.models import Laporan


class ProductForm(ModelForm):
    class Meta:
        model = Laporan
        fields = ["name","description"]