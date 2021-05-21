from django.test import TestCase, TransactionTestCase
from http import HTTPStatus
from django.urls import reverse
from tests.utils import TestClient as Client
# from rest_framework.test import APIClient as Client
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from HUAWEI.models import User, Site


# Include an appropriate `Authorization:` header on all requests.

class TestFee(TransactionTestCase):
    fixtures = ['test.json']
    user = [{
                'username': 'client1',
                'password': 'client1',
                'user_type': 0
            },
            {
                'username': 'manage1',
                'password': 'manage1',
                'user_type': 1
            },
            {
                'username': 'network1',
                'password': 'network1',
                'user_type': 2
            }]

    def test_get_fee(self):
        client = Client()
        assert client.get(reverse('fee')).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[0])
        client.get(reverse('flow_generate'))
        assert client.get(reverse('fee')).status_code == status.HTTP_200_OK
        client.login(**self.user[2])
        client.get(reverse('flow_generate'))
        assert client.get(reverse('fee')).status_code == status.HTTP_200_OK
