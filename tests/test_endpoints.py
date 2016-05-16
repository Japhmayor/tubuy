from rest_framework.test import APITestCase, APIClient
from api.models.user import User


class APIResourcesTestCase(APITestCase):
    """Testcase for the tubuy API"""

    def setUp(self):
        self.client = APIClient()

        # create test user
        self.user = User.objects.create_user(
            phone_number='+254701234567',
            password='tester',
            username='tester'
            )

        # obtain token for test user
        user_token = self.client.post(
            '/auth/',
            {'phone_number': '+254701234567', 'password': 'tester'}
            )
        self.token = user_token.data['token']

    def test_tubuy_api_endpoint(self):
        """test that the api endpoint is self documenting"""

        response = self.client.get('/api/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data['users'],
            'http://testserver/api/users/'
            )
        self.assertEqual(
            response.data['commodities'],
            'http://testserver/api/commodities/'
            )
        self.assertEqual(
            response.data['contributions'],
            'http://testserver/api/contributions/'
            )

    def test_tubuy_users_endpoint(self):
        """test for the user endpoint"""

        response = self.client.get('/api/users/')

        self.assertEqual(response.status_code, 200)

    def test_tubuy_commodity_endpoint(self):
        """test for the commodity endpoint"""

        before_auth_response = self.client.get('/api/commodities/')

        # before authentication
        self.assertEqual(before_auth_response.status_code, 403)

        # after authentication
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        after_auth_response = self.client.get('/api/commodities/')
        self.assertEqual(after_auth_response.status_code, 200)

    def test_tubuy_contribution_endpoint(self):
        """test for the contributions endpoint"""

        before_auth_response = self.client.get('/api/contributions/')

        # before authentication
        self.assertEqual(before_auth_response.status_code, 403)

        # after authentication
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        after_auth_response = self.client.get('/api/contributions/')
        self.assertEqual(after_auth_response.status_code, 200)
