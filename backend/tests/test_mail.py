from django.test import TestCase
from django.urls import reverse
from tests.utils import TestClient


class MailTests(TestCase):

    new_client: TestClient
    user = {
        'username': 'client1',
        'password': 'client1',
        "user_type": 0
    }

    def setUp(self):
        self.new_client = TestClient()

    def test_send(self):
        data = {}
        data['username'] = 'client1'
        data['email'] = 'thunder_network@126.com'
        responce = self.new_client.post(reverse('edit'), data=data, content_type="application/json")
        self.assertEqual(responce.status_code, 401)