from rest_framework import generics

from cards.models import Card
from .serializers import CardSerializer

__all__ = (
    'CardListCreateAPIView',
    'CardRetrieveUpdateDestroyAPIView',
)


class CardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
