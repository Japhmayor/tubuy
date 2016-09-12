from django.core.validators import MinValueValidator
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

    def update(self, instance, validated_data):
        """updates a user
        """
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class CommoditySerializer(serializers.ModelSerializer):
    """Serializer for commodity model
    """

    uuid = serializers.UUIDField(read_only=True, format='hex')
    requestor = serializers.ReadOnlyField(source='requestor.username')
    price = serializers.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
        )
    commodity_qr = serializers.ImageField(use_url=True, read_only=True)
    funded = serializers.BooleanField(read_only=True)
    remaining_amount = serializers.DecimalField(
        max_digits=8,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = Commodity
        fields = (
            'url',
            'commodity_qr',
            'uuid',
            'name',
            'description',
            'requestor',
            'funded',
            'price',
            'remaining_amount'
        )
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
    amount = serializers.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
        )

    class Meta:
        model = Contribution
        fields = ('amount', 'contributer', 'contributing_to')
