from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
import uuid
import base64
import random
import time
from io import BytesIO
import pyqrcode
from PIL import Image
from api.models.user import User


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
        request = pyqrcode.create(
            '{0}.{1}.{2}'.format(str(self.uuid), self.price, salt),
            version=10
            )
        encoded_request = request.png_as_base64_str()
        image = Image.open(
            BytesIO(base64.b64decode(encoded_request.encode()))
            )
        filename = '{0}.{1}'.format(
            str(time.time())[:10],
            (image.format).lower()
        )
        memory_image = BytesIO()
        image.save(memory_image, format=image.format)
        qr_file = InMemoryUploadedFile(
            memory_image,
            None,
            filename,
            'image/png',
            memory_image.tell,
            None
        )
        self.commodity_qr.save(
            filename,
            qr_file,
            save=False,
        )
        super(Commodity, self).save(**kwargs)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.requestor, self.name, self.price)
