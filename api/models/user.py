from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
    )
from django.core import validators
from django.db import models
import uuid
import re


class UserManager(BaseUserManager):
    """Manager class for the custom user model
    """

    class Meta:
        app_label = 'api'

    def create_user(self, phone_number, username=None, password=None):
        """Override the default create_user() method
        """

        account = self.model(phone_number=phone_number, username=username)
        account.set_password(password)
        account.save()
        return account


class User(AbstractBaseUser, PermissionsMixin):
    """Model defining the user
    """

    class Meta:
        app_label = 'api'

    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(
        max_length=254,
        validators=[validators.RegexValidator(
            re.compile('^[\w.@+-]+$'),
            'Enter a valid username.',
            'invalid'
        )]
    )
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    def __unicode__(self):
        return self.username
