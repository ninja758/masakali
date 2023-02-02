from django.contrib.auth.models import User
from rest_framework import serializers
from . models import otpModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'mobile']

class otpGeneratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = otpModel
        fields = []
