from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from tests.utils import TestClient as Client
from rest_framework import status
import time
from HUAWEI.models import User, Site


# Include an appropriate `Authorization:` header on all requests.

class TicketSite(TestCase):
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

    ticket = {
        "question": "这是一个新的测试提问",
        "question_type": 0,
        "site_name": "site0",
        "eq_name": ""
    }

    bad_ticket = {
        "question": "这是一个新的测试提问",
        "question_type": 0,
        "site_name": "wrong_site",
        "eq_name": ""
    }

    user_put = {
        "id": 3
    }
    network_put = {
        "id": 2,
        "answer": "这是一个新的测试回答"
    }

    detail_pk = 0
    # 超出范围
    bad_detail_pk = 9

    def test_get_ticket(self):
        client = Client()
        assert client.get(reverse('ticket')).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[1])
        assert client.get(reverse('ticket')).status_code == status.HTTP_403_FORBIDDEN
        client.logout()
        client.login(**self.user[0])
        assert client.get(reverse('ticket')).status_code == status.HTTP_200_OK
        client.logout()
        client.login(**self.user[2])
        assert client.get(reverse('ticket')).status_code == status.HTTP_200_OK

    def test_post_ticket(self):
        client = Client()
        assert client.post(reverse('ticket'), data=self.ticket).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[1])
        assert client.post(reverse('ticket'), data=self.ticket).status_code == status.HTTP_403_FORBIDDEN
        client.logout()
        client.login(**self.user[0])
        assert client.post(reverse('ticket'), data=self.ticket).status_code == status.HTTP_201_CREATED
        assert client.post(reverse('ticket'), data=self.bad_ticket).status_code == status.HTTP_400_BAD_REQUEST

    def test_put_ticket(self):
        client = Client()
        assert client.put(reverse('ticket'), data=self.user_put).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[1])
        assert client.put(reverse('ticket'), data=self.user_put).status_code == status.HTTP_403_FORBIDDEN
        client.logout()
        client.login(**self.user[0])
        assert client.put(reverse('ticket'), data=self.user_put).status_code == status.HTTP_200_OK
        assert client.put(reverse('ticket'), data=self.network_put).status_code == status.HTTP_400_BAD_REQUEST
        client.logout()
        client.login(**self.user[2])
        assert client.put(reverse('ticket'), data=self.network_put).status_code == status.HTTP_200_OK
        assert client.put(reverse('ticket'), data=self.user_put).status_code == status.HTTP_400_BAD_REQUEST
        client.logout()