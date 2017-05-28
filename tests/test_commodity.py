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

    def test_commodity_is_funded_if_remaining_amount_is_no_more_that_zero(self):
        """ a commodity can only be funded if the remaining_amount is <= 0
        """
        commodity =  {
            "name": "test commodity",
            "description": "test commodity description",
            "price": 100
        }

        commodity_response = self.client.post(
            reverse('api:commodity-list'),
            commodity
        )

        # make initial contribution

        contribution = {
            'contributing_to': commodity['name'],
            'amount': 50
        }
        initial_contrib_response = self.client.post(
            reverse('api:contribution-list'),
            contribution,
        )

        self.assertEqual(initial_contrib_response.status_code, 201)

        # check status of funding
        funded_commodity_response = self.client.get(
            reverse('api:commodity-detail', args=[commodity_response.data.get('uuid')])
        )

        self.assertEqual(funded_commodity_response.status_code, 200)
        self.assertEqual(funded_commodity_response.data.get('funded'), False)
        self.assertEqual(
            funded_commodity_response.data.get('remaining_amount'),
            "{:.2f}".format(commodity['price'] - contribution['amount'])
        )

        final_contrib_response = self.client.post(
            reverse('api:contribution-list'),
            contribution,
        )

        funded_commodity_response = self.client.get(
            reverse('api:commodity-detail', args=[commodity_response.data.get('uuid')])
        )

        self.assertEqual(funded_commodity_response.data.get('funded'), True)
