from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse

from api.models.user import User
from api.models.contribution import Contribution

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

        self.commodity = self.client.post(
            reverse('api:commodity-list'),
            {
                "name": "test commodity",
                "description": "test commodity description",
                "price": 100
            }
        )

    def test_making_negative_contribution_not_possible(self):
        """ ensure that user cannot pass a negative value as a contribution
        amount
        """
        contribution = {
            'contributing_to': self.commodity.data['name'],
            'amount': -10
        }
        response = self.client.post(
            reverse('api:contribution-list'),
            contribution,
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data.get('amount'),
            ["Ensure this value is greater than or equal to 0.01."]
        )
