from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from tests.utils import TestClient as Client
from rest_framework import status


# Include an appropriate `Authorization:` header on all requests.

class TestFlow(TransactionTestCase):
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

    def test_get_top_flow(self):
        client = Client()
        assert client.get(reverse('top_site_flow')).status_code == status.HTTP_401_UNAUTHORIZED
        client.login(**self.user[0])
        client.get(reverse('flow_generate'))
        assert client.get(reverse('top_site_flow')).status_code == status.HTTP_200_OK
        client.login(**self.user[2])
        client.get(reverse('flow_generate'))
        assert client.get(reverse('top_site_flow')).status_code == status.HTTP_200_OK

