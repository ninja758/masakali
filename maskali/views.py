import logging
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status


logging.basicConfig(level=logging.DEBUG)

User = get_user_model()


class CustomUserAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            user_object = {
                'username': user.id,
                'date_joined': user.date_joined,
                'last_login': user.last_login,
            }
            return Response({'token': token.key, 'user': user_object})
        return Response(
            {
                "message": "This request cannot be processed as it is invalid",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
