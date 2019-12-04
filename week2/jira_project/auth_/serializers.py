from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from auth_.models import MainUser
from auth_.token import get_token
import logging

logger = logging.getLogger(__name__)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('login', 'password')

    def complete(self):
        return MainUser.objects.create_user(
            login=self.validated_data['login'],
            password=self.validated_data['password'])


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('id', 'login', 'name')

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

    def validate(self, attrs):
        try:
            user = MainUser.objects.get(login=attrs['email'])
        except MainUser.DoesNotExist:
            logger.warning(f"Does not exist user with email: {attrs['email']}")
            raise ValidationError('Credentials are not correct.')
        if not check_password(attrs['password'], user.password):
            raise ValidationError('Credentials are not correct.')
        attrs['user'] = user
        return attrs

    # def validate_email(self, value):
    #     try:
    #         user = MainUser.objects.get(login=value)
    #     except MainUser.DoesNotExist:
    #         logger.warning(f"Does not exist user with email: {value}")
    #         raise ValidationError('Credentials are not correct.')
    #     return value

    def login(self):
        user = self.validated_data.get('user')
        return get_token(user), user
