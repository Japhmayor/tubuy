from rest_framework import viewsets
from api.models.user import User
from api.models.commodity import Commodity
from api.models.contribution import Contribution
from api.serializers import (
    UserSerializer,
    CommoditySerializer,
    ContributionSerializer
    )


class UserViewset(viewsets.ModelViewSet):
    """viewset for the user model
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = ('uuid')


class CommodityViewset(viewsets.ModelViewSet):
    """viewset for the commodity model
    """

    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer

    def perform_create(self, serializer):
        """sets the currently logged in user as requestor
        """
        user = User.objects.get(uuid=self.request.user.uuid)
        serializer.save(requestor=user)


class ContributionViewset(viewsets.ModelViewSet):
    """viewset for the contribution model
    """

    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

    def perform_create(self, serializer):
        """sets the currently logged in user as contributer
        """

        user = User.objects.get(uuid=self.request.user.uuid)
        serializer.save(contributer=user)
