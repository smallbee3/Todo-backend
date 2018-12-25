from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token

from utils.exceptions import CustomAPIException

User = get_user_model()

__all__ = (
    'UserSerializer',
)


class UserSerializer(serializers.ModelSerializer):

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

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise CustomAPIException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Password does not match the confirm password',
            )
        errors = dict()
        try:
            validate_password(password=attrs['password'])
        except ValidationError as e:
            errors['password'] = list(e.messages)
            raise serializers.ValidationError(errors)
            # raise CustomAPIException(
            #     status_code=status.HTTP_400_BAD_REQUEST,
            #     detail=errors,
            # )
        attrs.pop('password_confirm')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if self.context.get('request') \
                and self.context['request']._request.path == '/user/'\
                and self.context['request']._request.method == 'POST':
            token, _ = Token.objects.get_or_create(user=instance)
            ret['token'] = token.key
        return ret
