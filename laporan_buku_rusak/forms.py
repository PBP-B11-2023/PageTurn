from django.forms import ModelForm
<<<<<<< HEAD
from laporan_buku_rusak.models import Laporan
=======

from laporan_buku_rusak.models import Laporan

>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8

class ProductForm(ModelForm):
    class Meta:
        model = Laporan
<<<<<<< HEAD
        fields = ["name","description"]
=======
        fields = ["name","description"]
>>>>>>> 0831863604b29370ccf99c9f6f27fee495059be8
