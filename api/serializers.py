from api.models.user import User
from api.models.commodity import Commodity
from api.models.contribution import Contribution
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model
    """

    uuid = serializers.UUIDField(read_only=True, format='hex')
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = (
            'url',
            'uuid',
            'username',
            'password',
            'phone_number',
            'email',
            )
        extra_kwargs = {
            'url': {'lookup_field': 'uuid'}
        }

    def create(self, validated_data):
        """creates a user
        """
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CommoditySerializer(serializers.ModelSerializer):
    """Serializer for commodity model
    """

    uuid = serializers.UUIDField(read_only=True, format='hex')
    requestor = serializers.ReadOnlyField(source='requestor.username')
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    description = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Commodity
        fields = ('url', 'uuid', 'name', 'description', 'requestor', 'price')
        extra_kwargs = {
            'url': {'lookup_field': 'uuid'}
        }


class ContributionSerializer(serializers.ModelSerializer):
    """Serializer for contribution model
    """

    contributer = serializers.ReadOnlyField(source='contributer.username')
    contributing_to = serializers.SlugRelatedField(
        queryset=Commodity.objects.all(),
        slug_field='name'
        )

    class Meta:
        model = Contribution
        fields = ('amount', 'contributer', 'contributing_to')
