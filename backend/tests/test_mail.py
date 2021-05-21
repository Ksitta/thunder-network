from django.test import TestCase
from django.urls import reverse
from tests.utils import TestClient
from HUAWEI.models import User

class MailTests(TestCase):
    fixtures = ['test.json']

    new_client: TestClient
    user = {
        'username': 'client1',
        'password': 'client1',
        "user_type": 0
    }

    def setUp(self):
        self.new_client = TestClient()

    def test_send(self):
        self.new_client.post(reverse('token'), data=self.user, content_type="application/json")
        data = {'mory': 1}
        responce = self.new_client.post(reverse('mail'), data=data, content_type="application/json")
        self.assertEqual(responce.status_code, 200)