from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token

from utils.exceptions import CustomAPIException

User = get_user_model()

__all__ = (
    'UserCreateSerializer',
)


class UserCreateSerializer(serializers.ModelSerializer):

    nickname = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'password',
            'password_confirm',
            'nickname',
        )

    def validate_password(self, password):
        if password != self.initial_data['password_confirm']:
            raise CustomAPIException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Password does not match the confirm password',
            )
        errors = dict()
        try:
            validate_password(password=password)
        except ValidationError as e:
            errors['password'] = list(e.messages)
            raise serializers.ValidationError(errors)
            # raise CustomAPIException(
            #     status_code=status.HTTP_400_BAD_REQUEST,
            #     detail=errors,
            # )
        # attrs.pop('password_confirm')
        return password

    def create(self, validated_data):
        nickname = validated_data['username'].split('@')[0]
        validated_data.pop('password_confirm')
        validated_data['nickname'] = nickname
        return User.objects.create_django_user(**validated_data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        token, _ = Token.objects.get_or_create(user=instance)
        ret['token'] = token.key
        return ret
