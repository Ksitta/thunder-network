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


class Equipment(models.Model):
    eq_id = models.CharField('设备id', max_length=50, unique=True)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    eq_name = models.CharField('设备名称', max_length=20)
    eq_status = models.IntegerField('设备状态')


class EquipmentFlow(models.Model):
    eq_id = models.ForeignKey('Equipment', on_delete=models.CASCADE, blank=False)
    total_up = models.IntegerField('上行总流量', default=0)
    total_down = models.IntegerField('下行总流量', default=0)
    flow_1 = models.CharField('时段1', max_length=1000)
    flow_2 = models.CharField('时段2', max_length=1000)
    flow_3 = models.CharField('时段3', max_length=1000)
    flow_4 = models.CharField('时段4', max_length=1000)
    flow_5 = models.CharField('时段5', max_length=1000)
    flow_6 = models.CharField('时段6', max_length=1000)
    rate_unit = models.CharField('速率单位', max_length=10, default='byte')


class SiteFlow(models.Model):
    site_id = models.ForeignKey('Site', on_delete=models.CASCADE, blank=False)
    total_up = models.IntegerField('上行总流量', default=0)
    total_down = models.IntegerField('下行总流量', default=0)
    flow_1 = models.CharField('时段1', max_length=1000)
    flow_2 = models.CharField('时段2', max_length=1000)
    flow_3 = models.CharField('时段3', max_length=1000)
    flow_4 = models.CharField('时段4', max_length=1000)
    flow_5 = models.CharField('时段5', max_length=1000)
    flow_6 = models.CharField('时段6', max_length=1000)
    rate_unit = models.CharField('速率单位', max_length=10, default='byte')


class RawFlowData(models.Model):
    source_ip = models.GenericIPAddressField('源ip地址')
    dest_ip = models.GenericIPAddressField('目标ip地址')
    out_flow = models.IntegerField('出口流量')
    in_flow = models.IntegerField('入口流量')
