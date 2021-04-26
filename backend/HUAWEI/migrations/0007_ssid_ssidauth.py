# Generated by Django 3.1 on 2021-04-26 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HUAWEI', '0006_auto_20210424_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSID_id', models.CharField(max_length=50, unique=True, verbose_name='SSID_id')),
                ('name', models.CharField(max_length=20, verbose_name='SSID名称')),
                ('enable', models.BooleanField(default=True, verbose_name='开启状态')),
                ('maxUserNumber', models.IntegerField(verbose_name='最大用户数')),
                ('relativeRadios', models.IntegerField(verbose_name='射频类型')),
                ('userSeparation', models.BooleanField(default=False, verbose_name='用户隔离')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HUAWEI.site')),
            ],
        ),
        migrations.CreateModel(
            name='SSIDAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=10, verbose_name='认证模式')),
                ('pskEncryptType', models.CharField(max_length=20, verbose_name='安全模式')),
                ('securityKey', models.CharField(max_length=64, verbose_name='psk秘钥')),
                ('securityKeyType', models.CharField(max_length=10, verbose_name='加密方法')),
                ('SSID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HUAWEI.ssid')),
            ],
        ),
    ]
