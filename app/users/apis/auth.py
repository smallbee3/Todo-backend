from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer

User = get_user_model()

__all__ = (
    'UserLoginAPIView',
    'UserLogoutAPIView',
)


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        data = {
            'user': UserSerializer(user).data,
            'token': token.key,
        }
        return Response(data)


class UserLogoutAPIView(APIView):
    def post(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response('The user has been logout', status=status.HTTP_204_NO_CONTENT)
