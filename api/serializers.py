from api.models.user import UserProfile
from api.models.commodity import Commodity
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user information"""

    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True
    )

    class Meta:
        model = UserProfile
        fields = ('uuid', 'username', 'url', 'email', 'password')
        write_only_fields = ('email', 'password',)

    def create(self, validated_data):
        """Modify default method to create user."""
        return User.create_userprofile(**validated_data)


class CommoditySerializer(serializers.ModelSerializer):
    """Serializer for user commodity"""

    requestor = serializers.ReadOnlyField(source='requestor.username')
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Commodity
        fields = ('url', 'name', 'requestor', 'price')
