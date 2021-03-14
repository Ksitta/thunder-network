from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import User
import json


def responce(code: int, message: str):
    return JsonResponse(
        {
            'code': code,
            'message': message
        }
    )


def register(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            user_id = body['user_id']
            user_name = body['user_name']
            hash_password = body['hash_password']
            contact_details = body['contact_details']
            contact_email = body['contact_email']
            contact_address = body['contact_address']
            user = User.objects.filter(user_id=user_id)
            if user.exists():
                return responce(400, 'User id existed')
            User.objects.create(user_id=user_id, user_name=user_name, hash_password=hash_password,
                                contact_details=contact_details, contact_email=contact_email,
                                contact_address=contact_address)
            return responce(201, 'success')
        except:
            return responce(400, 'Parameter error')
    else:
        return responce(405, 'Error')


def delete_user(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            user_id = body['user_id']
            hash_password = body['hash_password']
            user = User.objects.get(user_id=user_id)
            if hash_password == user.hash_password:
                user.delete()
                return responce(201, "Success")
        except:
            return responce(400, "User not found")


def login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            user_id = body['user_id']
            hash_password = body['hash_password']
            user = User.objects.get(user_id=user_id)
            if hash_password == user.hash_password:
                return responce(201, "Success")
            return responce(400, "Error password")
        except:
            return responce(400, "User not found")
