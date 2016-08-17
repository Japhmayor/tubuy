from django.db import models
import uuid
from api.models.user import User
from api.models.commodity import Commodity
# from api.util import generate_qr


class Contribution(models.Model):
    """Contribution model defining co-buyers and their contribution
    """

    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    contributer = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    contributing_to = models.ForeignKey(Commodity)
    time = models.DateTimeField(auto_now_add=True)
    parent_block = models.CharField(max_length=70)

    def save(self, **kwargs):
        """overrides the save method for the model
        """
        last_contribution = Contribution.objects.all().last()
        self.parent_block = 0 if not last_contribution else last_contribution.uuid
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
