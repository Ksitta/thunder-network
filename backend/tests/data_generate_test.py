from datetime import datetime, timedelta

from django.urls import reverse
from HUAWEI import models
from tests.utils import TestClient as Client


class GenerateTool:
    """Generate data class"""
    admin_info = {
        'username': 'admin',
        'password': 'admin'
    }
    users = [
        {
            'username': 'client123',
            'password': 'client1',
            'user_type' : 0,
            'email': 'client1@thunder.com',
            'contact_details': '13900000000',
            'contact_email': '123@163.com',
            'contact_address': '2132131241234'
        }
    ]

    def generate_data(self):
        """Generate users"""
        self.generate_user()

    def generate_user(self):
        """Generate user"""
        client = Client()
        for user_info in self.users:
            res = client.post('/api/user/register/', data=user_info)
            print(res)
        print('finish user')
