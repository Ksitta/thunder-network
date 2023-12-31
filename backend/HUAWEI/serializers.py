from rest_framework import serializers
from . import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import exceptions
import re
try:
    from config.local_settings import register_number
except:
    pass


def validate_username(data):
    e = re.compile(r'^(?![^A-Za-z]+$)(?![^0-9]+$)[0-9A-Za-z_]{4,15}$')
    if not e.fullmatch(data):
        raise serializers.ValidationError('Enter a valid username.')
    return data


def validate_contact_details(data):
    e = re.compile(r'^1[3|4|5|7|8][0-9]{9}$')
    if not e.fullmatch(data):
        raise serializers.ValidationError('Enter a valid phone number.')
    return data


class UserRegisterSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.User

        fields = ['username', 'password', 'contact_details', 'contact_email', 'contact_address',
                  'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        user = models.User(
            username=validate_username(data['username']),
            user_type=data['user_type'],
            contact_details=validate_contact_details(data['contact_details']),
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
        extra_kwargs = {'username': {'read_only': True}, 'user_type': {'read_only': True}}

    def update(self, instance: models.User, data):
        instance.contact_address = data['contact_address']
        instance.contact_email = data['contact_email']
        instance.contact_details = validate_contact_details(data['contact_details'])
        instance.save()
        return instance


class PasswordEditSerializers(serializers.ModelSerializer):
    old_password = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['password', 'old_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if self.instance.check_password(attrs['old_password'] + str(self.instance.user_type)):
            return attrs
        raise serializers.ValidationError('原密码错误')

    def update(self, instance: models.User, data):
        new_pwd = data['password'] + str(instance.user_type)
        instance.set_password(new_pwd)
        instance.save()
        return instance


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Site
        fields = ['site_id', 'site_name', 'user', 'site_address', 'billing_level', 'demand_num', 'demand_1',
                  'demand_2', 'demand_3', 'status', 'create_time']

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

        fields = ['site_name', 'site_address', 'billing_level', 'demand_num', 'demand_1',
                  'demand_2', 'demand_3', 'status', 'user', 'create_time', 'manager_name',
                  'manager_time', 'network_name', 'network_time']


class FlowDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FlowData
        fields = ['eq', 'user', 'site', 'in_flow', 'out_flow', 'generate_time']


class EquipmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = ['eq_name', 'eq_status']


class SiteFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Site
        fields = ['site_name', 'rate_unit']


class EquipmentFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = ['eq_name', 'rate_unit']


class SSIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SSID
        fields = ['SSID_id', 'site', 'name', 'enable', 'maxUserNumber', 'relativeRadios', 'userSeparation']
    def create(self, validated_data):
        return models.SSID.objects.create(**validated_data)


class SSIDAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SSIDAuth
        fields = ['SSID', 'mode', 'pskEncryptType', 'securityKey', 'securityKeyType']
    def create(self, validated_data):
        return models.SSIDAuth.objects.create(**validated_data)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ['question', 'id', 'user', 'contact_details', 'contact_email', 'question_type', 'site_name', 'eq_name', 'status',
                  'create_time', 'answer', "network_name", "network_time", "close_time"]
    def create(self, validated_data):
        return models.Ticket.objects.create(**validated_data)