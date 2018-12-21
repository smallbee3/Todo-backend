from rest_framework import serializers

from .models import Card

__all__ = (
    'CardSerializer',
)


class CardSerializer(serializers.ModelSerializer):

    # contents = serializers.CharField()

    class Meta:
        model = Card
        fields = (
            'contents',
        )
