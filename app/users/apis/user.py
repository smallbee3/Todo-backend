from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from utils.permissions import IsSelfUserOrReadOnly
from ..serializers import (
    UserSerializer,
    UserCreateSerializer,
)

User = get_user_model()

__all__ = (
    'UserListCreateAPIView',
    'UserRetrieveUpdateDestroyAPIView',
)


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        else:
            return UserCreateSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
        IsSelfUserOrReadOnly,
    )
