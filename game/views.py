import logging
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status


logging.basicConfig(level=logging.DEBUG)

User = get_user_model()

class eventdetails(ObtainAuthToken):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response("Hello {0}!".format(request.user))

# Create your views here.
# get request to obtain event details
# get request to obtain last 10 games result
# post request to submit active game
# post request to transfer token
# last 10 transaction list
