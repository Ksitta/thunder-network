from django.test import TestCase
from django.urls import reverse
from tests.utils import TestClient


class UserModelTests(TestCase):
    new_client: TestClient

    fixtures = ['test.json']

    user = {
        'username': 'client1',
        'password': 'client1',
        "user_type": 0
    }

    pwd_change = {
        'username': 'pwd_change',
        'password': 'client1',
        "user_type": 0
    }

    wrong_pwd_user = {
        'username': 'client1',
        'password': 'error',
        "user_type": 0
    }

    none_user = {
        "username": "test4",
        "password": "none",
        "user_type": 0
    }

    new_user = {
        "username": "test2",
        "password": "123456",
        "user_type": 0,
        "contact_details": "13900000000",
        "contact_email": "123@163.com",
        "contact_address": "2132131241234"
    }

    error_user = {
        "username": "tes",
        "password": "123456",
        "user_type": 0,
        "contact_details": "139000000",
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

        response = self.new_client.post('/api/user/register/', data=self.error_user, content_type="application/json")
        self.assertEqual(response.status_code, 400)

        response = self.new_client.post('/api/user/register/', data=self.new_user, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_login(self):

        response = self.new_client.post(reverse('token'), data=self.none_user, content_type="application/json")
        self.assertEqual(response.status_code, 401)

        response = self.new_client.post(reverse('token'), data=self.wrong_pwd_user, content_type="application/json")
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

    def test_edit_pwd(self):
        response = self.new_client.post(reverse('token'), data=self.pwd_change, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        data = {
            "old_password": "client1",
            "password": "123456"
        }
        responce = self.new_client.post(reverse('edit'), data=data, content_type="application/json")
        self.assertEqual(responce.status_code, 201)
        response = self.new_client.post(reverse('token'), data=self.pwd_change, content_type="application/json")
        self.assertEqual(response.status_code, 401)
        new_user = self.pwd_change
        new_user['password'] = "123456"
        response = self.new_client.post(reverse('token'), data=new_user, content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.new_client.post('/api/user/register/', data=self.new_user, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.new_client.post(reverse('token'), data=self.new_user, content_type="application/json")
        response = self.new_client.delete(reverse('edit'), data=self.new_user, content_type="application/json")
        self.assertEqual(response.status_code, 204)


class ViewTests(TestCase):
    new_client: TestClient

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
