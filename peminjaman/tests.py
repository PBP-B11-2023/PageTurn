from django.test import TestCase, Client
from django.urls import reverse
from homepage.models import CustomUser
from katalog.models import Book
from django.contrib.auth import get_user_model

class CustomUserModelTest(TestCase):

    def test_create_user(self):
        CustomUser.objects.create_user(username='john', password='123')
        self.assertEqual(CustomUser.objects.count(), 1)
        
    def test_create_superuser(self):
        CustomUser.objects.create_superuser(username='john', password='123')
        self.assertEqual(CustomUser.objects.count(), 1)

class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='john', password='123')
        self.show_homepage_url = reverse('homepage:show_homepage')
        self.login_url = reverse('homepage:login')
        self.register_url = reverse('homepage:register')

    def test_show_homepage_GET(self):
        response = self.client.get(self.show_homepage_url)
        self.assertEqual(response.status_code, 200)

    def test_register_POST(self):
        response = self.client.post(self.register_url, {
            'username': 'johndoe',
            'password1': 'randompassword123',
            'password2': 'randompassword123',
        })
        self.assertEqual(CustomUser.objects.count(), 2) 

    def test_login_user_POST(self):
        self.client.login(username='john', password='123')
        response = self.client.post(self.login_url, {
            'username': 'john',
            'password': '123',
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful login

# Create your tests here.
