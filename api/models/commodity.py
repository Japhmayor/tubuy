from django.db import models
import random
import uuid
from api.models.user import User
from api.util import generate_qr


def upload_path(instance, filename):
    """sets the directory for storing QR codes
    """

    requestor = User.objects.get(uuid=instance.requestor.uuid)
    requestor_hex = requestor.uuid.hex
    file_path = "commodities/{0}/{1}".format(requestor_hex[-20:], filename)
    return file_path


class Commodity(models.Model):
    """Commodity model defining item to be co-buyied
    """

    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    requestor = models.ForeignKey(User, to_field='uuid')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=70)
    description = models.TextField()
    date_requested = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    funded = models.BooleanField(default=False)
    date_funded = models.DateField(blank=True, null=True)
    commodity_qr = models.ImageField(upload_to=upload_path, blank=True)
    remaining_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, **kwargs):
        """overrides the save method for the model
        """
        salt = (random.random() ** 2) * 10 ** 2
        generate_qr(self, salt)
        super(Commodity, self).save(**kwargs)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.requestor, self.name, self.price)
