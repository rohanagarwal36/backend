from rest_framework import serializers

from user_management_app.models import User, AuthDetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'age')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class AuthDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthDetails
        fields = ('key', 'id')
