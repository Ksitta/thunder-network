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

    eq = {
        "eq_num": 2,
        "eq_list": [
            {
                "eq_name": "ap1",
                "eq_status": 1
            },
            {
                "eq_name": "ap2",
                "eq_status": 1
            }
        ]
    }

    # bad_eq = {
    #     "eq_num": 2,
    #     "eq_list": [
    #         {
    #             "eq_name": "ap1",
    #             "eq_status": 1
    #         },
    #         {
    #             "eq_name": "ap2",
    #             "eq_status": 1
    #         }
    #     ]
    # }

    site_pk = 2
    # 超出范围
    bad_site_pk = 1

    def test_post_eq(self):
        client = Client()
        assert client.post(reverse('equipment', args=[self.site_pk]), data=self.eq).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[0])
        assert client.post(reverse('equipment', args=[self.site_pk]), data=self.eq).status_code == status.HTTP_403_FORBIDDEN
        client.logout()
        client.login(**self.user[2])
        assert client.post(reverse('equipment', args=[self.site_pk]), data=self.eq).status_code == status.HTTP_201_CREATED
        assert client.post(reverse('equipment', args=[self.site_pk]), data=self.eq).status_code == status.HTTP_400_BAD_REQUEST