from django.test import TestCase
from django.urls import reverse
from tests.utils import TestClient


class UserModelTests(TestCase):
    new_client: TestClient

    fixtures = ['test.json']

    user = {
        'username': 'client1',
        'password': 'client1'
    }

    none_user = {
        "username": "test",
        "password": "error_pwd"
    }

    new_user = {
        "username": "test",
        "password": "123456",
        "contact_details": "13900000000",
        "contact_email": "123@163.com",
        "contact_address": "2132131241234"
    }

    def setUp(self):

        self.new_client = TestClient()

    def test_register(self):

        response = self.new_client.post(reverse('token'), data=self.new_user, content_type="application/json")
        self.assertEqual(response.status_code, 401)

        response = self.new_client.post('/api/user/register/', data=self.new_user, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        response = self.new_client.post('/api/user/register/', data=self.new_user, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_login(self):

        response = self.new_client.post(reverse('token'), data=self.none_user, content_type="application/json")
        self.assertEqual(response.status_code, 401)

        response = self.new_client.post(reverse('token'), data=self.user, content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_profile(self):

        self.new_client.logout()
        response = self.new_client.get(reverse('profile'))
        self.assertEqual(response.status_code, 401)

        self.new_client.post(reverse('token'), data=self.user, content_type="application/json")
        response = self.new_client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        info = response.json()['user']
        self.assertEqual(info["contact_details"], "13900000000")
        self.assertEqual(info["contact_email"], "123@163.com")
        self.assertEqual(info["contact_address"], "2132131241234")

    def test_edit(self):
        response = self.new_client.post(reverse('token'), data=self.user, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        data = {
            "contact_details": "13700000000",
            "contact_email": "abc@qq.com",
            "contact_address": "thu"
        }
        responce = self.new_client.put(reverse('edit'), data=data, content_type="application/json")
        self.assertEqual(responce.status_code, 204)

        self.new_client.post(reverse('token'), data=self.user, content_type="application/json")
        response = self.new_client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        info = response.json()['user']
        self.assertEqual(info["contact_details"], "13700000000")
        self.assertEqual(info["contact_email"], "abc@qq.com")
        self.assertEqual(info["contact_address"], "thu")



class ViewTests(TestCase):
    new_client: TestClient

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
