from django.forms import ModelForm

from review.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description"]