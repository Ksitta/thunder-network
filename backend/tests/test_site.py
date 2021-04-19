from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from tests.utils import TestClient as Client
from rest_framework import status
import time
from HUAWEI.models import User, Site

# Include an appropriate `Authorization:` header on all requests.

class TestSite(TestCase):
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

    bad_site = {
        'site_name': site['site_name'],
        'site_address': '清华大学',
        'billing_level': 1,
        'demand_num': 2,
        'demand_1': 'Guest',
        'demand_2': 'Management',
        'demand_3': '',
    }

    assign_network = {
        'network_name': 'network1',
    }

    detail_pk = 0
    # 超出范围
    bad_detail_pk = 9

    def test_get_site_list(self):
        client = Client()
        assert client.get(reverse('site')).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[0])
        assert client.get(reverse('site')).status_code == status.HTTP_200_OK
    
    def test_post_site(self):
        client = Client()
        assert client.post(reverse('site'), data=self.site).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[0])
        assert client.post(reverse('site'), data=self.site).status_code == status.HTTP_201_CREATED
        assert client.post(reverse('site'), data=self.bad_site).status_code == status.HTTP_400_BAD_REQUEST

    def test_get_site_detail(self):
        client = Client()
        assert client.get(reverse('site_detail',
                          args=[self.detail_pk])).status_code == HTTPStatus.UNAUTHORIZED
        client.login(**self.user[0])
        assert client.get(reverse('site_detail',
                          args=[self.bad_detail_pk])).status_code == status.HTTP_400_BAD_REQUEST
        assert client.get(reverse('site_detail',
                          args=[self.detail_pk])).status_code == status.HTTP_200_OK

    def test_post_site_detail(self):
        client = Client()
        assert client.post(reverse('site_detail',
                          args=[self.detail_pk]), data=self.assign_network).status_code == HTTPStatus.UNAUTHORIZED
        client.login(**self.user[0])
        assert client.post(reverse('site_detail',
                          args=[self.detail_pk]), data=self.assign_network).status_code == status.HTTP_403_FORBIDDEN
        client.logout()
        client.login(**self.user[1])
        assert client.post(reverse('site_detail', args=[0]), data=self.assign_network).status_code == status.HTTP_400_BAD_REQUEST
        assert client.post(reverse('site_detail', args=[1]), data=self.assign_network).status_code == status.HTTP_200_OK


    def test_z_delete_site(self):
        client = Client()
        assert client.delete(reverse('site_detail',
                          args=[self.detail_pk])).status_code == HTTPStatus.UNAUTHORIZED
        client.login(**self.user[0])
        assert client.delete(reverse('site_detail',
                          args=[self.detail_pk])).status_code == status.HTTP_403_FORBIDDEN
        client.logout()
        client.login(**self.user[1])
        assert client.delete(reverse('site_detail',
                          args=[self.detail_pk])).status_code == status.HTTP_204_NO_CONTENT