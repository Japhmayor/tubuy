from django.conf.urls import url, include
from rest_framework import routers
from api import viewsets

router = routers.DefaultRouter()
router.register(r'users',  viewsets.UserlistViewset)
router.register(r'commodities',  viewsets.CommodityViewset)
router.register(r'contributions',  viewsets.ContributionViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
