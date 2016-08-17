from django.core.files.uploadedfile import InMemoryUploadedFile
import base64
import time
from io import BytesIO
import pyqrcode
from PIL import Image


def generate_qr(commodity, salt):
    """generates an in-memory QR code based off commodity
    """
    remainder = commodity.remaining_amount
    request = pyqrcode.create(
        '{0}.{1}.{2}.{3}'.format(
            str(commodity.uuid),
            commodity.price,
            salt,
            remainder
            ),
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
    commodity.commodity_qr.save(
        filename,
        qr_file,
        save=False,
    )

    return commodity
