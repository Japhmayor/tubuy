from django.db import models
from djmoney.models.fields import MoneyField
from .user import UserProfile


class Commodity(models.Model):
    """Commodity model defining item to be co-buyied"""

    price = MoneyField(
        decimal_places=2,
        max_digits=8,
        default_currency='KES'
    )
    name = models.CharFieldCaseInsensitive(max_length=70)
    requestor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0} {1}'.format(self.name, self.price)
