from django.test import TestCase
from django.urls import reverse
from tests.utils import TestClient as Client
from rest_framework import status
from HUAWEI.models import Site, SSID
import time

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

    site = {
        'site_name': str(time.time()),
        'site_address': '清华大学',
        'billing_level': 1,
        'demand_num': 2,
        'demand_1': 'Guest',
        'demand_2': 'Management',
        'demand_3': '',
    }

    ssid = {
        "name": str(int(time.time())),
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
    bad_ssid1 = {
        "name": ssid['name'],
        "enable": True,
        "maxUserNumber": 20,
        "relativeRadios": 7,
        "userSeparation": False,
        "ssidAuth": {
            "mode": "psk",
            "pskEncryptType": "wpa2",
            "securityKey": "123",
            "securityKeyType": "AES"
        }
    }
    bad_ssid2 = {
        "name": ssid['name'],
        "enable": True,
        "maxUserNumber": 20,
        "relativeRadios": 7,
        "userSeparation": False,
        "ssidAuth": {
            "mode": "ppsk",
            "pskEncryptType": "wep",
            "securityKey": "123",
            "securityKeyType": "AES"
        }
    }
    bad_ssid3 = {
        "name": ssid['name'],
        "enable": True,
        "maxUserNumber": 20,
        "relativeRadios": 7,
        "userSeparation": False,
        "ssidAuth": {
            "mode": "psk",
            "pskEncryptType": "wep",
            "securityKey": "123456",
            "securityKeyType": "AES"
        }
    }
    long_ssid = {
        "name": "00000000000000000000000000",
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

    get_pk = 0
    site_pk = 4
    # 超出范围
    bad_site_pk = 1

    def test_get_SSID(self):
        client = Client()
        assert client.get(reverse('ssid', args=[self.get_pk])).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[0])
        assert client.get(reverse('ssid', args=[self.bad_site_pk])).status_code == status.HTTP_400_BAD_REQUEST
        assert client.get(reverse('ssid', args=[self.get_pk])).status_code == status.HTTP_200_OK
        client.logout()
        client.login(**self.user[1])
        assert client.get(reverse('ssid', args=[self.get_pk])).status_code == status.HTTP_200_OK
        client.logout()
        client.login(**self.user[2])
        assert client.get(reverse('ssid', args=[self.get_pk])).status_code == status.HTTP_200_OK
        client.logout()

    def test_post_SSID(self):
        client = Client()
        assert client.post(reverse('ssid', args=[self.site_pk]), data=self.ssid).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[0])
        assert client.post(reverse('ssid', args=[self.get_pk]), data=self.ssid).status_code == status.HTTP_400_BAD_REQUEST
        assert client.post(reverse('ssid', args=[self.bad_site_pk]), data=self.ssid).status_code == status.HTTP_400_BAD_REQUEST
        client.post(reverse('site'), data=self.site)
        the_site = Site.objects.filter(id=Site.objects.last().id)[0]
        the_site.status = 0
        the_site.save()
        assert client.post(reverse('ssid', args=[self.site_pk]),
                           data=self.ssid).status_code == status.HTTP_201_CREATED
        assert client.post(reverse('ssid', args=[self.site_pk]),
                           data=self.bad_ssid1).status_code == status.HTTP_400_BAD_REQUEST
        assert client.post(reverse('ssid', args=[self.site_pk]),
                           data=self.bad_ssid2).status_code == status.HTTP_400_BAD_REQUEST
        assert client.post(reverse('ssid', args=[self.site_pk]),
                           data=self.bad_ssid3).status_code == status.HTTP_400_BAD_REQUEST
        assert client.post(reverse('ssid', args=[self.site_pk]),
                           data=self.long_ssid).status_code == status.HTTP_400_BAD_REQUEST
        client.logout()
        client.login(**self.user[1])
        assert client.post(reverse('ssid', args=[self.site_pk]),
                           data=self.ssid).status_code == status.HTTP_403_FORBIDDEN
        client.logout()