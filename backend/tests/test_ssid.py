from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from tests.utils import TestClient as Client
# from rest_framework.test import APIClient as Client
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from HUAWEI.models import User, Site
import time


# Include an appropriate `Authorization:` header on all requests.

class TestSSID(TestCase):
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

    ssid = {
        "name": str(time.time()),
        "enable": True,
        "maxUserNumber": 20,
        "relativeRadios": 7,
        "userSeparation": False,
        "ssidAuth": {
            "mode": "psk",
            "pskEncryptType": "wpa2",
            "securityKey": "12345678",
            "securityKeyType": "AES"
        }
    }
    bad_ssid = {
        "name": ssid['name'],
        "enable": True,
        "maxUserNumber": 20,
        "relativeRadios": 7,
        "userSeparation": False,
        "ssidAuth": {
            "mode": "psk",
            "pskEncryptType": "wpa2",
            "securityKey": "12345678",
            "securityKeyType": "AES"
        }
    }

    site_pk = 0
    # 超出范围
    bad_site_pk = 1

    def test_post_SSID(self):
        client = Client()
        assert client.post(reverse('ssid', args=[self.site_pk]), data=self.ssid).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[0])
        assert client.post(reverse('ssid', args=[self.bad_site_pk]), data=self.ssid).status_code == status.HTTP_400_BAD_REQUEST
        assert client.post(reverse('ssid', args=[self.site_pk]), data=self.ssid).status_code == status.HTTP_201_CREATED
        assert client.post(reverse('ssid', args=[self.site_pk]), data=self.bad_ssid).status_code == status.HTTP_400_BAD_REQUEST