from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        )


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)

