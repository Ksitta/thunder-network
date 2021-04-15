# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    contact_details = models.CharField('联系方式', max_length=12)
    contact_email = models.CharField('邮箱', max_length=20)
    contact_address = models.CharField('客户地址', max_length=100)
    user_type = models.IntegerField(default=0)


class Site(models.Model):
    site_id = models.CharField('站点id', max_length=50, unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True)
    site_name = models.CharField('站点名称', max_length=20)
    site_address = models.CharField('站点地址', max_length=100)
    billing_level = models.IntegerField('计费等级')
    demand_num = models.IntegerField('需求数量')
    demand_1 = models.CharField('需求1', max_length=20, blank=True)
    demand_2 = models.CharField('需求2', max_length=20, blank=True)
    demand_3 = models.CharField('需求3', max_length=20, blank=True)
    status = models.IntegerField('订单、部署状态')
    create_time = models.DateTimeField(auto_now_add=True)
    manager_name = models.CharField('运营工程师', max_length=50, default="", blank=True)
    manager_time = models.DateTimeField(null=True, default=None, blank=True)
    network_name = models.CharField('网络工程师', max_length=50, default="", blank=True)
    network_time = models.DateTimeField(null=True, default=None, blank=True)

    total_up = models.IntegerField('上行总流量', default=0)
    total_down = models.IntegerField('下行总流量', default=0)
    flow_data = models.CharField('流量数据', max_length=1000, default="{}")
    rate_unit = models.CharField('速率单位', max_length=10, default='byte')


class Equipment(models.Model):
    eq_id = models.CharField('设备id', max_length=50, unique=True)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    eq_name = models.CharField('设备名称', max_length=20)
    eq_status = models.IntegerField('设备状态')
    total_up = models.IntegerField('上行总流量', default=0)
    total_down = models.IntegerField('下行总流量', default=0)
    flow_data = models.CharField('流量数据', max_length=1000, default="{}")
    rate_unit = models.CharField('速率单位', max_length=10, default='byte')


class RawFlowData(models.Model):
    source_ip = models.GenericIPAddressField('源ip地址')
    dest_ip = models.GenericIPAddressField('目标ip地址')
    out_flow = models.IntegerField('出口流量')
    in_flow = models.IntegerField('入口流量')
