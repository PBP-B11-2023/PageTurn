from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from homepage.models import CustomUser
from katalog.models import Book
from laporan_buku_rusak.models import Laporan
from peminjaman.models import Peminjaman


class MainTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.User = get_user_model()
        self.user = self.User.objects.create_user(username='testuser')
        self.user.set_password('testpassword')
        self.user.save()
        self.laporan = Laporan.objects.create(user=self.user, name="tes", description="tes")

    def test_main_using_main_template_1(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
