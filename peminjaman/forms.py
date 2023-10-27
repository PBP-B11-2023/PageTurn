from django import forms

from .models import Peminjaman


class PeminjamanForm(forms.ModelForm):
    durasi_peminjaman = forms.IntegerField(label='Durasi Peminjaman (dalam hari)', min_value=1, max_value=14)

    class Meta:
        model = Peminjaman
        fields = ['durasi_peminjaman']
