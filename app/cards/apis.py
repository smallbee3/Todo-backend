from rest_framework import generics, permissions

from cards.models import Card
from utils.permissions import IsOwnerOrReadOnly

from .serializers import CardSerializer

__all__ = (
    'CardListCreateAPIView',
    'CardRetrieveUpdateDestroyAPIView',
)


class CardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly,
    )
