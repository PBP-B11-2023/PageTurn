from django.urls import path
from review.views import create_product_flutter, show_json, show_main
from review.views import show_main, create_review
from review.views import edit_review
from review.views import delete_review
from review.views import get_review_json, add_review_ajax

app_name = 'review_buku'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-review', create_review, name='create_review'),
    path('edit-review/<int:id>', edit_review, name='edit_review'),
    path('delete/<int:id>', delete_review, name='delete_review'), # sesuaikan dengan nama fungsi yang dibuat
    path('get-review/', get_review_json, name='get_review_json'),
    path('create-product-ajax/', add_review_ajax, name='add_review_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('json/', show_json, name='show_json'),
]