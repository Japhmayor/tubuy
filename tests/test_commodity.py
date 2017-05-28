from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse

from api.models.user import User

class APIUsersTestCase(APITestCase):
    """Testcase for users on tubuy
    """

    def setUp(self):
        # create test user
        self.user = User.objects.create_user(
            phone_number='+254701234567',
            password='tester',
            username='tester'
            )

        # obtain token for test user
        user_token = self.client.post(
            '/token-auth/',
            {'phone_number': '+254701234567', 'password': 'tester'}
            )
        self.token = user_token.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)


    def test_creating_commodity_with_negative_price_not_possible(self):
        """ ensure that user cannot pass a negative value as a commodity
        price
        """
        commodity =  {
            "name": "test commodity",
            "description": "test commodity description",
            "price": -100
        }

        response = self.client.post(
            reverse('api:commodity-list'),
            commodity
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data.get('price'),
            ["Ensure this value is greater than or equal to 0.01."]
        )
