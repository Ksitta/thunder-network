from django.test import TestCase
from HUAWEI.models import User
import json
from tests.utils import TestClient


class UserModelTests(TestCase):
    token: str
    new_client: TestClient

    def setUp(self):
        self.new_client = TestClient()

    def test_register(self):
        data = {
            "username": "test",
            "password": "123456",
            "contact_details": "13900000000",
            "contact_email": "123@163.com",
            "contact_address": "2132131241234"
        }
        response = self.new_client.post('/api/user/register/', data=data, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        response = self.new_client.post('/api/user/register/', data=data, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        data = {
            "username": "test",
            "password": "error_pwd"
        }
        response = self.new_client.post('/api/user/token/', data=data, content_type="application/json")
        self.assertEqual(response.status_code, 401)

        # data = {
        #     "username": "test",
        #     "password": "test_pwd"
        # }
        # response = self.new_client.post('/api/user/token/', data=data, content_type="application/json")
        # self.assertEqual(response.status_code, 201)

    def test_profile(self):
        self.new_client.logout()
        response = self.new_client.get('/api/user/profile/')
        self.assertEqual(response.status_code, 401)
        # data = {
        #     "username": "test",
        #     "password": "test_pwd"
        # }
        # self.new_client.post('/api/user/token/', data=data, content_type="application/json")
        # response = self.new_client.get('/api/user/profile/')
        # self.assertEqual(response.status_code, 201)


class ViewTests(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
