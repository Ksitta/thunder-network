from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from tests.utils import TestClient as Client
from rest_framework import status
import time
from HUAWEI.models import User, Site


# Include an appropriate `Authorization:` header on all requests.

class TestAssign(TestCase):
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
    
    site_pk = 1
    bad_site_pk = 0

    assign_network = {
        'network_name': 'network1',
    }


    def test_get_assign(self):
        client = Client()
        assert client.get(reverse('assign',
                          args=[self.site_pk])).status_code == HTTPStatus.UNAUTHORIZED
        client.login(**self.user[0])
        assert client.get(reverse('assign', args=[self.site_pk])).status_code == status.HTTP_403_FORBIDDEN
        client.logout()
        client.login(**self.user[1])
        assert client.get(reverse('assign', args=[self.bad_site_pk])).status_code == status.HTTP_400_BAD_REQUEST
        assert client.get(reverse('assign', args=[9])).status_code == status.HTTP_400_BAD_REQUEST
        assert client.get(reverse('assign', args=[self.site_pk])).status_code == status.HTTP_200_OK

    def test_post_assign(self):
        client = Client()
        assert client.post(reverse('assign', args=[self.site_pk]), data=self.assign_network).status_code == HTTPStatus.UNAUTHORIZED
        client.login(**self.user[0])
        assert client.post(reverse('assign', args=[self.site_pk]), data=self.assign_network).status_code == status.HTTP_403_FORBIDDEN
        client.logout()
        client.login(**self.user[1])
        assert client.post(reverse('assign', args=[self.bad_site_pk]), data=self.assign_network).status_code == status.HTTP_400_BAD_REQUEST
        assert client.post(reverse('assign', args=[self.site_pk]), data=self.assign_network).status_code == status.HTTP_200_OK
