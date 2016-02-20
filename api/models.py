from __future__ import unicode_literals

from django.db import models
from djmoney.models.fields import MoneyField
import uuid


class User(models.Model):
    """User model defining buyers and co-buyers"""

    unique_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


class Commodity(models.Model):
    """Commodity model defining item to be co-buyied"""

    price = MoneyField(
        decimal_places=2,
        max_digits=8,
        default_currency='KES'
    )

    requestor = models.ForeignKey(User, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Contribution(models.Model):
    """ Contribution model defining co-buyers and total amout raised"""

    contribution = MoneyField(
        decimal_places=2,
        max_digits=8,
    )

    co_buyer = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True)
