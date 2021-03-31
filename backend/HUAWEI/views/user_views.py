from django.shortcuts import render

# Create your views here.
from HUAWEI.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from HUAWEI.serializers import UserRegisterSerializers, TokenObtainSerializer, UserProfileSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenViewBase


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializers


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializers(request.user)
        return Response({'user': serializer.data}, 200)

    def put(self, request):
        user = request.user
        info = UserProfileSerializers(user, data=request.data)
        info.is_valid(True)
        info.save()
        return Response("Success", 204)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response("Success", 204)


class TokenObtainView(TokenViewBase):
    serializer_class = TokenObtainSerializer

