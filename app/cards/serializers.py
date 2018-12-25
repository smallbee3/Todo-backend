from rest_framework import serializers

from .models import Card

__all__ = (
    'CardSerializer',
)


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = (
            'pk',
            'contents',
            'owner',
        )
