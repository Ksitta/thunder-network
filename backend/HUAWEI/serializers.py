from rest_framework import serializers
from . import models


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        read_only_fields = ['username']
        fields = ['contact_details', 'contact_email', 'contact_address'] + read_only_fields

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
        #validated_data.
        return models.Site.objects.create(**validated_data)
