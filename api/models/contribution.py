from django.db import models
from djmoney.models.fields import MoneyField
from .user import UserProfile


class Contribution(models.Model):
    """ Contribution model defining co-buyers and total amout raised"""

    amount = MoneyField(
        decimal_places=2,
        max_digits=8,
    )

    co_buyer = models.ForeignKey(UserProfile)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{0} {1}'.format(self.co_buyer, self.amount)
