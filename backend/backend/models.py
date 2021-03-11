# models.py
from django.db import models


class Test(models.Model):
    user_name = models.CharField('用户名', max_length=20)
    hash_password = models.CharField('哈希密码', max_length=128, null=True, blank=True)