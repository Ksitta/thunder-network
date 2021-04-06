from rest_framework import serializers
from . import models
from .models import User, Equipment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import exceptions


class UserRegisterSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['username', 'password', 'contact_details', 'contact_email', 'contact_address', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        user = User(
            username=data['username'],
            user_type=data['user_type'],
            contact_details=data['contact_details'],
            contact_email=data['contact_email'],
            contact_address=data['contact_address'],
        )
        pwd = data['password'] + str(data['user_type'])
        user.set_password(pwd)
        user.save()
        return user


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['contact_details', 'contact_email', 'contact_address', 'username', 'user_type']
        extra_kwargs = {'username': {'read_only': True}, 'user_type': {'read_only' : True}}

    def update(self, instance: User, data):
        instance.contact_address = data['contact_address']
        instance.contact_email = data['contact_email']
        instance.contact_details = data['contact_details']
        instance.save()
        return instance


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Site
        fields = ('site_id', 'site_name', 'user', 'site_address', 'billing_level', 'demand_num', 'demand_1',
                  'demand_2', 'demand_3', 'status')

    def create(self, validated_data):
        """
        基础功能中，暂时自动为其生成AP设备、且自动返回订单成功
        之后应注意修改为，网络工程师同意后才成功
        """
        # validated_data.

        return models.Site.objects.create(**validated_data)


class TokenObtainSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'key_error': "用户名或密码错误"
    }

    def validate(self, attrs):
        auth_args = {
            'username': attrs['username'],
            'password': attrs['password'],
            'request': self.context['request']}

        user = authenticate(**auth_args)
        if user is None:
            raise exceptions.AuthenticationFailed(
                self.error_messages['key_error'],
                'key_error',
            )

        data = {}
        refresh = self.get_token(user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = ['eq_id', 'site', 'eq_name', 'eq_status']

    def create(self, validated_data):
        return models.Equipment.objects.create(**validated_data)

class SiteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Site
        fields = ('site_name', 'site_address', 'billing_level', 'demand_num', 'demand_1',
                  'demand_2', 'demand_3', 'status')

class EquipmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = ['eq_name', 'eq_status']
