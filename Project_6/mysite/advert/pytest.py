from django.test import TestCase
from .models import Advert
import requests
from django.test.client import Client

def test_advert(self):
    user = Advert.Advert.objects.create(user_id=3, name="Test", content="Tests")
    assert user.user_id == "test_1"
    assert user.name == "test_1"
    assert user.content == "test_1"

def test_view(self):
    response = requests.get('http://127.0.0.1:8000/adverts/view/')
    response.raise_for_status()
    assert  response.status_code == 200
    assert not  response.is_redirect


def test_login(self):
    response = requests.get('http://127.0.0.1:8000/users/login/')
    response.raise_for_status()
    assert  response.status_code == 200
    assert not  response.is_redirect