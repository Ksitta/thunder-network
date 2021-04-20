from django.shortcuts import render

# Create your views here.
from HUAWEI.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from HUAWEI.serializers import UserRegisterSerializers, TokenObtainSerializer, UserProfileSerializers, PasswordEditSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializers


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializers(request.user)
        return Response({'user': serializer.data}, 200)

    def post(self, request):
        user = request.user
        serializer = PasswordEditSerializers(user, data=request.data)
        serializer.is_valid(True)
        serializer.save()
        return Response('success', 201)

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

    def post(self, request, *args, **kwargs):
        request.data['password'] += str(request.data['user_type'])
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
