from django.test import TestCase
'''
class UserModelTests(TestCase):
    def setUp(self):
        pass

    def register(self):
        data = {}
        data['username'] = 'test'
        data['password'] = '123455'
        data['contact_detail'] = '1234560'
        data['contact_email'] = '123@163.com'
        data['contact_address'] = 'asdasd'
        return self.client.post('/api/user/register',
                                data=data, content_type="application/json")
'''
class ViewTests(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)