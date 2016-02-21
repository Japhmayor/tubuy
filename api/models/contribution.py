from django.db import models
from .user import UserProfile
from .commodity import Commodity


class Contribution(models.Model):
    """ Contribution model defining co-buyers and total amout raised"""

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    co_buyer = models.ForeignKey(UserProfile)
    contributing_to = models.ForeignKey(Commodity, default="6009")
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{0} {1}'.format(self.co_buyer, self.amount)
