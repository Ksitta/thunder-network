# Generated by Django 3.1 on 2021-05-04 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HUAWEI', '0007_ssid_ssidauth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=500, verbose_name='问题描述')),
                ('site_name', models.CharField(default='', max_length=50, verbose_name='站点名')),
                ('status', models.IntegerField(verbose_name='处理状态')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('answer', models.CharField(blank=True, default='', max_length=500, verbose_name='解答反馈')),
                ('network_name', models.CharField(blank=True, default='', max_length=50, verbose_name='网络工程师')),
                ('network_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('close_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]