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
    site_pk = 0
    # 超出范围
    bad_site_pk = 1

    def test_get_site_flow(self):
        client = Client()
        assert client.get(reverse('site_flow', args=[self.site_pk])).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[2])
        client.get(reverse('flow_generate'))
        assert client.get(reverse('site_flow', args=[self.site_pk])).status_code == status.HTTP_200_OK
        assert client.get(reverse('site_flow', args=[self.bad_site_pk])).status_code == status.HTTP_400_BAD_REQUEST