from django.shortcuts import render

# Create your views here.
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import UserRegisterSerializers, TokenObtainSerializer, UserProfileSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenViewBase


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializers

    def list(self, request, *args, **kwargs):
        return Response('不存在API', 404)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            serializer = UserProfileSerializers(request.user)
            return Response({'user': serializer.data}, 200)
        except:
            return Response("Not login", 400)


class UserOperationView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        info = UserProfileSerializers(user, data=request.data)
        info.is_valid(True)
        info.save()
        return Response("Success", 204)

    def delete(self, request):
        try:
            user = request.user
            user.delete()
            return Response("Success", 204)
        except:
            return Response("Error", 404)


class TokenObtainView(TokenViewBase):
    serializer_class = TokenObtainSerializer

