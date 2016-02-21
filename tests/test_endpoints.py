from rest_framework.test import APITestCase, APIClient


class APIResourcesTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_tubuy_api_endpoint(self):
        response = self.client.get('/api/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['users'], 'http://testserver/api/users/')

    def test_tubuy_users_endpoint(self):
        response = self.client.get('/api/users/')

        self.assertEqual(response.status_code, 200)

    def test_tubuy_commodity_endpoint(self):
        response = self.client.get('/api/commodity/')

        self.assertEqual(response.status_code, 200)

    def test_tubuy_contribution_endpoint(self):
        response = self.client.get('/api/contribution/')

        self.assertEqual(response.status_code, 200)
