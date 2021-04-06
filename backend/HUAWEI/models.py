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
    eq_id = models.CharField('设备id', max_length=50, unique=True)
    terminal_num = models.IntegerField('终端数量')
    up_rate = models.IntegerField('上行速率')
    down_rate = models.IntegerField('下行速率')
    rate_unit = models.CharField('速率单位', max_length=10)


class SiteFlow(models.Model):
    site_id = models.CharField('站点id', max_length=50, unique=True)
    user_num_2_4 = models.IntegerField('2.4G用户数量')
    user_num_5 = models.IntegerField('5G用户数量')
    up_rate = models.IntegerField('上行速率')
    down_rate = models.IntegerField('下行速率')
    rate_unit = models.CharField('速率单位', max_length=10)

