from django.db import models
from api.models.user import User
from api.models.commodity import Commodity


class Contribution(models.Model):
    """Contribution model defining co-buyers and their contribution
    """

    contributer = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    contributing_to = models.ForeignKey(Commodity, default="1")
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{0} {1}'.format(self.contributer, self.amount)
