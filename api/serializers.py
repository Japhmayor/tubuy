from api.models.user import UserProfile
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
        import ipdb; ipdb.set_trace()
        return User.create_userprofile(**validated_data)
