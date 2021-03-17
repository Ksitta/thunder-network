from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from HUAWEI.models import User
import json
from django.contrib import auth
from rest_framework.response import Response
from rest_framework.views import APIView
from HUAWEI.serializers import UserProfileSerializers
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication


class UserProfileView(APIView):
    def get(self, request):
        try:
            serializer = UserProfileSerializers(request.user)
            return Response({'user': serializer.data}, 200)
        except:
            return Response("Not login", 400)

    def post(self, request):
        body = json.loads(request.body)
        try:
            username = body['username']
            password = body['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                request.session.set_expiry(0)
                return Response("Success", 201)
            return Response("Error password", 400)
        except:
            return Response("User not found", 400)


class UserOperationView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        body = json.loads(request.body)
        try:
            username = body['username']
            password = body['password']
            contact_details = body['contact_details']
            contact_email = body['contact_email']
            contact_address = body['contact_address']
            user = User.objects.filter(username=username)
            if user.exists():
                return Response('User id existed', status=400)
            User.objects.create_user(username=username, password=password, contact_details=contact_details,
                                     contact_email=contact_email, contact_address=contact_address)
            return Response('success', 201)
        except:
            return Response('Parameter error', 400)

    def put(self, request):
        pass

    def delete(self, request):
        try:
            user = request.user
        except:
            return Response("Error", 404)
        user.delete()
        return Response("Success", 204)
