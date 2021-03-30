from http import HTTPStatus
from django.test.client import Client
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


class TestClient(Client):

    def __init__(self, enforce_csrf_checks=False, **defaults):
        super().__init__(enforce_csrf_checks, **defaults)
        self.token = {}
        self.auto_refresh = True
        self.username = None

    def get(self, path, data=None, follow=False, secure=False, **extra):
        """Override get"""
        if self.auto_refresh and not extra.get('refresh'):
            self.refresh()
        params = locals()
        params.pop('self')
        token = extra.pop('token', None)
        if token and 'access' in token:
            self.token = token
        if self.token:
            params['HTTP_AUTHORIZATION'] = 'Bearer ' + self.token['access']
        return super().get(**params)

    def post(self, path, data=None, content_type='application/json',
             follow=False, secure=False, **extra):
        """Override post"""
        if self.auto_refresh and not extra.get('refresh'):
            self.refresh()
        params = locals()
        params.pop('self')
        token = extra.pop('token', None)
        if token and 'access' in token:
            self.token = token
        if self.token:
            params['HTTP_AUTHORIZATION'] = 'Bearer ' + self.token['access']
        if not params['content_type']:
            params.pop('content_type')
        response = super().post(**params)
        if getattr(response, 'data', None) and 'access' in response.data:
            self.token.update(response.data)
        return response

    def delete(self, path, data='', content_type='application/json',
               follow=False, secure=False, **extra):
        """Override delete"""
        if self.auto_refresh and not extra.get('refresh'):
            self.refresh()
        params = locals()
        params.pop('self')
        token = extra.pop('token', None)
        if token and 'access' in token:
            self.token = token
        if self.token:
            params['HTTP_AUTHORIZATION'] = 'Bearer ' + self.token['access']
        if not params['content_type']:
            params.pop('content_type')
        return super().delete(**params)

    def login(self, **credentials):
        """Login for jwt"""
        if self.post(reverse('auth'), credentials).status_code == HTTPStatus.OK:
            self.username = credentials.get('username')
            return True
        return False

    def force_login(self, user, backend=None):
        refresh = RefreshToken.for_user(user)

        self.token['access'] = str(refresh.access_token)
        self.token['refresh'] = str(refresh)

    def refresh(self):
        """Refresh the token"""
        refresh = self.token.get('refresh')
        if not refresh:
            return False
        return self.post(reverse('refresh'), data={'refresh': refresh}, refresh=True).status_code == HTTPStatus.OK

    def logout(self):
        """Logout by clear token"""
        self.token = {}
        self.username = None