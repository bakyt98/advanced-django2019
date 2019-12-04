from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import MainUser
from auth_.serializers import (RegisterSerializer, MainUserSerializer,
                               LoginSerializer)


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.complete()
    return Response(MainUserSerializer(user).data)


@api_view(['GET'])
def login(request):
    serializer = LoginSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    token, user = serializer.login()
    return Response({'token': token,
                     'user': MainUserSerializer(user).data})


class MainUserAPIView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.complete()
        return Response(MainUserSerializer(user).data)

    def get(self, request):
        serializer = LoginSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        token, user = serializer.login()
        return Response({'token': token,
                         'user': MainUserSerializer(user).data})
