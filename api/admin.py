from django.contrib import admin
from api.models.user import UserProfile, User

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(User)
