from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from user_management_app.models import User


class ApiTest(APITestCase):
    def setUp(self):
        extra_fields = {'first_name': 'first', 'last_name': 'last'}
        self.user = User.objects._create_user('test@xyz.com', 'password', 23, **extra_fields)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))

    def test_login(self):
        url = reverse('login')
        data = {'email': self.user.email, 'password': 'password'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # can't check key as it is randomly generated
        self.assertContains(response, 'key')

    def test_logout(self):
        url = reverse('logout')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        url = reverse('create-user')
        data = {'email': 'user1@xyz.com',
                'password': 'password',
                'age': 23,
                'first_name': 'first',
                'last_name': 'last'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_data = {'id': 2,
                         'email': 'user1@xyz.com',
                         'age': 23,
                         'first_name': 'first',
                         'last_name': 'last'}
        self.assertEqual(response.data, expected_data)

    def test_get(self):

        url = reverse('get-update', args=[self.user.id, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {'id': self.user.id,
                         'email': 'test@xyz.com',
                         'age': 23,
                         'first_name': 'first',
                         'last_name': 'last'}
        self.assertEqual(response.data, expected_data)

    def test_update(self):

        url = reverse('get-update', args=[self.user.id, ])
        data = {'email': 'test@xyz.com',
                'password': 'password',
                'age': 32,
                'first_name': 'first',
                'last_name': 'last'}
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {'id': self.user.id,
                         'email': 'test@xyz.com',
                         'age': 32,
                         'first_name': 'first',
                         'last_name': 'last'}
        self.assertEqual(response.data, expected_data)
