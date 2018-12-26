from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Card

User = get_user_model()

__all__ = (
    'CardSerializer',
)


class CardSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = Card
        fields = (
            'pk',
            'contents',
            'owner',
        )
