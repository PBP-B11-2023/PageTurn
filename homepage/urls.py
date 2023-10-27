from django.urls import path

from homepage.views import *

app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get_favourite_books/',get_favourite_books, name='get_favourite_books'),
]
