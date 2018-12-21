from rest_framework import generics

from cards.models import Card
from .serializers import CardSerializer

__all__ = (
    'CardListCreateView',
    'CardRetrieveUpdateDestroyView',
)


class CardListCreateView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
