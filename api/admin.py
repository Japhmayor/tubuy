from django.contrib import admin
from api.models.user import User
from api.models.commodity import Commodity
from api.models.contribution import Contribution

# Register your models here.
admin.site.register(User)
admin.site.register(Commodity)
admin.site.register(Contribution)
