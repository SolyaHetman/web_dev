from django.core.exceptions import NON_FIELD_ERRORS
from django.test import TestCase
from .models import Advert
import requests
from django.test.client import Client

# Create your tests here.
class AdvertTestCase(TestCase):

    def setUp(self):
        Advert.objects.create( user_id =3, name = "Test",content="Tests")

    def test_advert(self):
        user = Advert.objects.get()
        self.assertEqual(user.user_id, 3)
        self.assertEqual(user.name,"Test")
        self.assertEqual(user.content,"Tests")


class UrlsTestCase(TestCase):
    def test_view(self):
        response = requests.get('http://127.0.0.1:8000/adverts/view/')
        self.assertEqual(response.status_code,200)

    def test_loin(self):
        response = requests.get('http://127.0.0.1:8000/users/login/')
        self.assertEqual(response.status_code,200)

class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('http://127.0.0.1:8000/adverts/view/')
        self.assertEqual(response.status_code, 200)

class TestCalls(TestCase):
    def test_call_view_loads(self):
        self.client.login(username='user', password='test')  # defined in fixture or with factory in setUp()
        response = self.client.get('/adverts/view/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advert/advert_list.html')





