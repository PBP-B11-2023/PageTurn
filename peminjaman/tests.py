import json

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from homepage.models import CustomUser
from katalog.models import Book
from peminjaman.models import Peminjaman


class TemplateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.User = get_user_model()
        self.user = self.User.objects.create_user(username='testuser')
        self.user.set_password('testpassword')
        self.user.save()

    def test_main_using_main_template_1(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/peminjaman/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peminjaman.html')

    def test_main_using_main_template_2(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/peminjaman/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_peminjaman.html')

    def test_main_using_main_template_2(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/peminjaman/history/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'history_peminjaman.html')

    def test_main_using_main_template_2(self):
        response = self.client.get('/peminjaman/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'guest_peminjaman.html')

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.User = get_user_model()
        self.user = self.User.objects.create_user(username='testuser')
        self.user.set_password('testpassword')
        self.user.save()
        self.book = Book.objects.get(pk=1)
        self.p_ret = Peminjaman.objects.create(user=self.user, book=self.book, is_returned=True)
        self.p_not_ret = Peminjaman.objects.create(user=self.user, book=self.book, is_returned=False)

    def test_add_peminjaman_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('peminjaman:add_peminjaman'))
        
        # Periksa konteks respons
        self.assertEqual(response.context['books'].count(), 89)
        self.assertEqual(response.context['books'].first(), self.book)
        
    def test_show_history_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('peminjaman:show_history'))
        
        # Periksa status kode HTTP respons
        self.assertEqual(response.status_code, 200)
        
        # Periksa template yang digunakan
        self.assertTemplateUsed(response, 'history_peminjaman.html')
        
        # Periksa konteks respons
        self.assertEqual(response.context['user'], self.user)
        self.assertEqual(response.context['books'].count(), 89)
        self.assertEqual(response.context['books'].first(), self.book)
        self.assertEqual(response.context['dikembalikan'].count(), 1)
        self.assertEqual(response.context['dikembalikan'].first(), self.p_ret)

    def test_get_json_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('peminjaman:get_item_json'))
        
        # Periksa status kode HTTP respons
        self.assertEqual(response.status_code, 200)
        
        # Periksa konten respons
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['fields']['user'], self.user.pk)

        response = self.client.get(reverse('peminjaman:get_item_json_returned'))
        
        # Periksa status kode HTTP respons
        self.assertEqual(response.status_code, 200)
        
        # Periksa konten respons
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['fields']['user'], self.user.pk)

        response = self.client.get(reverse('peminjaman:get_book_json'))
        
        # Periksa status kode HTTP respons
        self.assertEqual(response.status_code, 200)
        
        # Periksa konten respons
        data = json.loads(response.content)
        self.assertEqual(len(data), 89)
    
    def test_return_book_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        self.book.is_dipinjam = True
        self.book.cnt_dipinjam = 0
        self.book.save()

        response = self.client.post(reverse('peminjaman:return_book', args=[self.p_not_ret.pk]))
        
        # Periksa status kode HTTP respons
        self.assertEqual(response.status_code, 201)
        
        # Periksa efek samping dari request
        self.p_not_ret.refresh_from_db()
        self.assertTrue(self.p_not_ret.is_returned)
        
        self.book.refresh_from_db()
        self.assertFalse(self.book.is_dipinjam)
        self.assertEqual(self.book.cnt_dipinjam, 1)

        self.book.cnt_dipinjam = 0
        self.book.save()

        response = self.client.get(reverse('peminjaman:return_book', args=[self.p_not_ret.pk])) # pakai method get bkn post
        
        # Periksa status kode HTTP respons
        self.assertEqual(response.status_code, 404)  # 404 adalah status kode untuk "Not Found"

    def test_add_book_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('peminjaman:add_book', args=[self.book.pk]), {
            'durasi_peminjaman': 7,
        })
        
        # Periksa status kode HTTP respons
        self.assertEqual(response.status_code, 201)
        
        # Periksa efek samping dari request
        self.book.refresh_from_db()
        self.assertTrue(self.book.is_dipinjam)
        
        peminjaman = Peminjaman.objects.filter(book=self.book).last()
        self.assertEqual(peminjaman.user, self.user)
        self.assertEqual(peminjaman.durasi_peminjaman, 7)

        response = self.client.get(reverse('peminjaman:add_book', args=[self.book.pk])) # pakai method get bkn post
        
        # Periksa status kode HTTP respons
        self.assertEqual(response.status_code, 404)  # 404 adalah status kode untuk "Not Found"