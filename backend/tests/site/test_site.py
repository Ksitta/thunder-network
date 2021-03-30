from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from tests.utils import TestClient as Client
#from rest_framework.test import APIClient as Client
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from HUAWEI.models import User

# Include an appropriate `Authorization:` header on all requests.

class TestSite(TestCase):
    fixtures = ['test.json']
    user = {
        'username': 'client1',
        'password': 'client1'
    }

    detail_pk = 0
    # 超出范围
    wrong_detail_pk = 1

    def test_get_site_list(self):
        client = Client()
        assert client.get(reverse('site_list')).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user)
        assert client.get(reverse('site_list')).status_code == status.HTTP_200_OK

    # def test_get_site_detail(self):
    #     client = Client()
    #     assert client.get(reverse('site_detail'),
    #                       args=[self.user, self.detail_pk]).status_code == HTTPStatus.UNAUTHORIZED
    #     client.login(**self.user)
    #     assert client.get(reverse('site_detail'),
    #                       args=[client.user, self.detail_pk]).status_code == status.HTTP_200_OK
    #     assert client.get(reverse('site_detail'),
    #                       args=[client.user, self.wrong_detail_pk]).status_code == status.HTTP_400_BAD_REQUEST
