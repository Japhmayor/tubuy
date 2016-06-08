from django.db import models
from api.models.user import User
from api.models.commodity import Commodity


class Contribution(models.Model):
    """Contribution model defining co-buyers and their contribution
    """

    contributer = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    contributing_to = models.ForeignKey(Commodity)
    time = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        """overrides the save method for the model
        """
        commodity = self.contributing_to
        if not commodity.funded:
            commodity.remaining_amount -= self.amount
            commodity.funded = (False, True)[commodity.remaining_amount <= 0]
        else:
            commodity.remaining_amount -= self.amount
        commodity.save()
        super(Contribution, self).save(**kwargs)

    def __unicode__(self):
        return '{0} {1}'.format(self.contributer, self.amount)
