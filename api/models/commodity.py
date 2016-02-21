from django.db import models
from .user import UserProfile
from . import custom_model_field


class Commodity(models.Model):
    """Commodity model defining item to be co-buyied"""

    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = custom_model_field.CharFieldCaseInsensitive(max_length=70)
    requestor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0} {1}'.format(self.name, self.price)
