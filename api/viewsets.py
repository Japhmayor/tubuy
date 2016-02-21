from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models.user import UserProfile
from api.models.commodity import Commodity
from api.serializers import UserSerializer, CommoditySerializer
from django.db import IntegrityError


class UserlistViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        """Define customizations during user creation."""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                UserProfile.create_userprofile(**serializer.validated_data)
                return Response({
                    'message': 'user created'
                }, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({
                    'message': 'user with entered email already exists'
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'message': "user not created"
        }, status=status.HTTP_400_BAD_REQUEST)


class CommodityViewset(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer

    def perform_create(self, serializer):
        user = UserProfile.objects.get(id=self.request.user.id)
        serializer.save(requestor=user)
