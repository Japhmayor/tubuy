from django.conf.urls import url, include
from rest_framework import routers
from api import viewsets

router = routers.DefaultRouter()
router.register(r'users',  viewsets.UserlistViewset)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
