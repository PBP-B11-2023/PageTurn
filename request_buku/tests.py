from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from homepage.models import CustomUser
from katalog.models import Book
from peminjaman.models import Peminjaman
from request_buku.models import Request


class MainTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.User = get_user_model()
        self.user = self.User.objects.create_user(username='testuser')
        self.user.set_password('testpassword')
        self.user.save()
        self.request = Request.objects.create(title="tes", author="tes", description="tes")

    def test_show_main_GET(self):
        response = self.client.get('/request_buku/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'request_buku.html')

    def test_create_request_POST(self):
        response = self.client.get('/request_buku/create-request')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_request.html')
        response = self.client.post('/request_buku/create-request', {
            'title' : "tes",
            'author' : "tes",
            "description" : "tes",
        })

        self.assertEqual(response.status_code, 302)  # check if the status code is 302, which stands for redirection

    def test_get_request_json_GET(self):
        response = self.client.get('/request_buku/get-request/')

        self.assertEqual(response.status_code, 200)  # check if the status code is 200
        # check if the response contains the serialized data of the product
        self.assertContains(response, self.request.title)
        self.assertContains(response, self.request.author)
        self.assertContains(response, self.request.description)

    def test_add_review_ajax_POST(self):
        response = self.client.post('/request_buku/create-request-ajax/', {
            'title' : "tes",
            'author' : "tes",
            "description" : "tes",
        })

        self.assertEqual(response.status_code, 201)  # check if the status code is 201, which stands for created
        # check if a new product was created with the correct data
        self.assertTrue(Request.objects.filter(title='tes', author='tes', description='tes').exists())

        response = self.client.get('/request_buku/create-request-ajax/', {
            'title' : "tes",
            'author' : "tes",
            "description" : "tes",
        })

        self.assertEqual(response.status_code, 404)  # kalo bkn post bakal 404

    def test_delete(self):
        req2 = Request.objects.create(title="tes", author="tes", description="tes")
        req2.save()
        response = self.client.get('/request_buku/delete/'+str(req2.pk))
        self.assertEquals(response.status_code, 302)