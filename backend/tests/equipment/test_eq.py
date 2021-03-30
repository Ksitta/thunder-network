from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from tests.utils import TestClient as Client
# from rest_framework.test import APIClient as Client
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from HUAWEI.models import User, Site


# Include an appropriate `Authorization:` header on all requests.

class TestEquipment(TestCase):
    fixtures = ['test.json']
    user = {
        'username': 'client1',
        'password': 'client1'
    }
