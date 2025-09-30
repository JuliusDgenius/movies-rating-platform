from rest_framework import serializers
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class EmailTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = User.objects.filter(email__iexact=email).order_by('id').first()
        if not user:
            raise AuthenticationFailed('No active account found with the given credentials')

        if not user.is_active or not user.check_password(password):
            raise AuthenticationFailed('No active account found with the given credentials')

        refresh = RefreshToken.for_user(user)

        return {
            'access_token': str(refresh.access_token),
            'token_type': 'bearer',
        }
