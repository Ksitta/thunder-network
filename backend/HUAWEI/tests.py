from django.test import TestCase
from HUAWEI.models import User
import json

class UserModelTests(TestCase):
    token: str

    def setUp(self):
        pass

    def test_1_register(self):
        data = {
            "username": "test",
            "password": "123456",
            "contact_details": "13900000000",
            "contact_email": "123@163.com",
            "contact_address": "2132131241234"
        }
        response = self.client.post('/api/user/register/', data=data, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        data = {
            "username": "test",
            "password": "123456"
        }
        response = self.client.post('/api/user/token/', data=data, content_type="application/json")
        self.token = response.data['access']
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/api/user/profile')

    def test_2_login(self):
        data = {
            "username": "test",
            "password": "error_pwd"
        }
        response = self.client.post('/api/user/token/', data=data, content_type="application/json")
        self.assertEqual(response.status_code, 401)


class ViewTests(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
