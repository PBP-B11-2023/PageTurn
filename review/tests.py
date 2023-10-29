import json

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from review.models import Product


class MainTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.User = get_user_model()
        self.user = self.User.objects.create_user(username='testuser')
        self.user.set_password('testpassword')
        self.user.save()
        self.review1 = Product.objects.create(user = self.user, name="tes", description="tes")
    
    def test_show_main_GET(self):
        response = self.client.get('/review/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviewbuku.html')

    def test_create_review_POST(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/review/create-review')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_review.html')
        response = self.client.post('/review/create-review', {
            'name' : "tes",
            "description" : "tes",
        })

        self.assertEqual(response.status_code, 302)  # check if the status code is 302, which stands for redirection
        self.assertEqual(Product.objects.first().user, self.user)  # check if the product was created by the correct user

    def test_edit_review_POST(self):
        response = self.client.get('/review/edit-review/1')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_review.html')
        response = self.client.post('/review/edit-review/1', {
            'name': 'Updated product',
            'description': 'Updated description',
        })

        self.review1.refresh_from_db()  # refresh the product instance to get the updated data

        self.assertEqual(response.status_code, 302)  # check if the status code is 302, which stands for redirection
        self.assertEqual(self.review1.name, 'Updated product')  # check if the product name was updated
        self.assertEqual(self.review1.description, 'Updated description')  # check if the product description was updated

    def test_delete_review(self):
        review2 = Product.objects.create(user = self.user, name="tes", description="tes")
        id = review2.pk
        response = self.client.get('/review/delete/' + str(id))
        self.assertEquals(response.status_code, 302)

    def test_get_review_json_GET(self):
        response = self.client.get('/review/get-review/')

        self.assertEqual(response.status_code, 200)  # check if the status code is 200
        # check if the response contains the serialized data of the product
        self.assertContains(response, self.review1.name)
        self.assertContains(response, self.review1.description)

    def test_add_review_ajax_POST(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/review/create-product-ajax/', {
            'name': 'New product',
            'description': 'New description',
        })

        self.assertEqual(response.status_code, 201)  # check if the status code is 201, which stands for created
        # check if a new product was created with the correct data
        self.assertTrue(Product.objects.filter(name='New product', description='New description').exists())

        response = self.client.get('/review/create-product-ajax/', {
            'name': 'New product',
            'description': 'New description',
        })

        self.assertEqual(response.status_code, 404)  # kalo bkn post bakal 404