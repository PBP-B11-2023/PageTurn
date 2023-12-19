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
        response = self.client.get('/laporan_buku_rusak/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laporan_buku_rusak.html')

    def test_main_using_main_template_2(self):
        response = self.client.get('/laporan_buku_rusak/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tamu.html')

    def test_add_laporan_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('laporan_buku_rusak:add_product_ajax'), {
            'name': 'tes',
            'description' : 'tes',
        })
        # Periksa status kode HTTP respons
        self.assertEqual(response.status_code, 201)
    
        # # Periksa status kode HTTP respons
        response = self.client.get(reverse('laporan_buku_rusak:add_product_ajax'), {
            'name': 'tes',
            'description' : 'tes',
        })
        self.assertEqual(response.status_code, 404)  # 404 adalah status kode untuk "Not Found"
