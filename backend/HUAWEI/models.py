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
    rate_unit = models.CharField('速率单位', max_length=10, default='byte')


class Equipment(models.Model):
    eq_id = models.CharField('设备id', max_length=50, unique=True)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    eq_name = models.CharField('设备名称', max_length=20)
    eq_status = models.IntegerField('设备状态')
    rate_unit = models.CharField('速率单位', max_length=10, default='byte')


class FlowData(models.Model):
    source_ip = models.GenericIPAddressField('源ip地址')
    dest_ip = models.GenericIPAddressField('目标ip地址')
    out_flow = models.IntegerField('出口流量')
    in_flow = models.IntegerField('入口流量')
    eq = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    site = models.ForeignKey('Site', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    generate_time = models.IntegerField('时间戳')


class RawFlowData(models.Model):
    source_ip = models.GenericIPAddressField('源ip地址')
    dest_ip = models.GenericIPAddressField('目标ip地址')
    out_flow = models.IntegerField('出口流量')
    in_flow = models.IntegerField('入口流量')


class SSID(models.Model):
    SSID_id = models.CharField('SSID_id', max_length=50, unique=True)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    name = models.CharField('SSID名称', max_length=20)
    enable = models.BooleanField('开启状态', default=True)
    maxUserNumber = models.IntegerField('最大用户数')
    relativeRadios = models.IntegerField('射频类型')
    userSeparation = models.BooleanField('用户隔离', default=False)


class SSIDAuth(models.Model):
    SSID = models.ForeignKey('SSID', on_delete=models.CASCADE)
    mode = models.CharField('认证模式', max_length=10)
    pskEncryptType = models.CharField('安全模式', max_length=20)
    securityKey = models.CharField('psk秘钥', max_length=64)
    securityKeyType = models.CharField('加密方法', max_length=10)


class Ticket(models.Model):
    question = models.CharField('问题描述', max_length=500, default="")
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    question_type = models.IntegerField('问题类型', default=0)
    site_name = models.CharField('站点名', max_length=50, default="")
    eq_name = models.CharField('设备名', max_length=50, default="")
    status = models.IntegerField('处理状态')
    create_time = models.DateTimeField(auto_now_add=True)
    answer = models.CharField('解答反馈', max_length=500, default="", blank=True)
    network_name = models.CharField('网络工程师', max_length=50, default="", blank=True)
    network_time = models.DateTimeField(null=True, default=None, blank=True)
    close_time = models.DateTimeField(null=True, default=None, blank=True)
