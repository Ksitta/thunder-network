from django.test import TestCase


class UserModelTests(TestCase):
    Token: str

    def setUp(self):
        pass

    def test_register(self):
        data = {
            "username": "k11t3123",
            "password": "12346",
            "contact_details": "13900000000",
            "contact_email": "123@163.com",
            "contact_address": "2132131241234"
        }
        response = self.client.post('/api/user/register/', data=data, content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        pass

class ViewTests(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
