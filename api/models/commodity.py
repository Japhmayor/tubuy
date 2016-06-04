from django.db import models
import uuid
from api.models.user import User


class Commodity(models.Model):
    """Commodity model defining item to be co-buyied
    """

    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    requestor = models.ForeignKey(User)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=70)
    description = models.TextField()
    date_requested = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    funded = models.BooleanField(default=False)
    date_funded = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.requestor, self.name, self.price)
