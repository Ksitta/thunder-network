# Generated by Django 3.1 on 2021-04-13 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HUAWEI', '0010_auto_20210413_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentflow',
            name='down_rate',
        ),
        migrations.RemoveField(
            model_name='equipmentflow',
            name='out_flow_1',
        ),
        migrations.RemoveField(
            model_name='equipmentflow',
            name='out_flow_2',
        ),
        migrations.RemoveField(
            model_name='equipmentflow',
            name='out_flow_3',
        ),
        migrations.RemoveField(
            model_name='equipmentflow',
            name='out_flow_4',
        ),
        migrations.RemoveField(
            model_name='equipmentflow',
            name='out_flow_5',
        ),
        migrations.RemoveField(
            model_name='equipmentflow',
            name='out_flow_6',
        ),
        migrations.RemoveField(
            model_name='equipmentflow',
            name='terminal_num',
        ),
        migrations.RemoveField(
            model_name='equipmentflow',
            name='total_flow',
        ),
        migrations.RemoveField(
            model_name='equipmentflow',
            name='up_rate',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='down_rate',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='out_flow_1',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='out_flow_2',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='out_flow_3',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='out_flow_4',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='out_flow_5',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='out_flow_6',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='total_flow',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='up_rate',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='user_num_2_4',
        ),
        migrations.RemoveField(
            model_name='siteflow',
            name='user_num_5',
        ),
        migrations.AddField(
            model_name='equipmentflow',
            name='total_down',
            field=models.IntegerField(default=0, verbose_name='下行总流量'),
        ),
        migrations.AddField(
            model_name='equipmentflow',
            name='total_up',
            field=models.IntegerField(default=0, verbose_name='上行总流量'),
        ),
        migrations.AddField(
            model_name='siteflow',
            name='total_down',
            field=models.IntegerField(default=0, verbose_name='下行总流量'),
        ),
        migrations.AddField(
            model_name='siteflow',
            name='total_up',
            field=models.IntegerField(default=0, verbose_name='上行总流量'),
        ),
        migrations.AlterField(
            model_name='equipmentflow',
            name='flow_1',
            field=models.CharField(max_length=1000, verbose_name='时段1'),
        ),
        migrations.AlterField(
            model_name='equipmentflow',
            name='flow_2',
            field=models.CharField(max_length=1000, verbose_name='时段2'),
        ),
        migrations.AlterField(
            model_name='equipmentflow',
            name='flow_3',
            field=models.CharField(max_length=1000, verbose_name='时段3'),
        ),
        migrations.AlterField(
            model_name='equipmentflow',
            name='flow_4',
            field=models.CharField(max_length=1000, verbose_name='时段4'),
        ),
        migrations.AlterField(
            model_name='equipmentflow',
            name='flow_5',
            field=models.CharField(max_length=1000, verbose_name='时段5'),
        ),
        migrations.AlterField(
            model_name='equipmentflow',
            name='flow_6',
            field=models.CharField(max_length=1000, verbose_name='时段6'),
        ),
        migrations.AlterField(
            model_name='equipmentflow',
            name='rate_unit',
            field=models.CharField(default='byte', max_length=10, verbose_name='速率单位'),
        ),
        migrations.AlterField(
            model_name='siteflow',
            name='flow_1',
            field=models.CharField(max_length=1000, verbose_name='时段1'),
        ),
        migrations.AlterField(
            model_name='siteflow',
            name='flow_2',
            field=models.CharField(max_length=1000, verbose_name='时段2'),
        ),
        migrations.AlterField(
            model_name='siteflow',
            name='flow_3',
            field=models.CharField(max_length=1000, verbose_name='时段3'),
        ),
        migrations.AlterField(
            model_name='siteflow',
            name='flow_4',
            field=models.CharField(max_length=1000, verbose_name='时段4'),
        ),
        migrations.AlterField(
            model_name='siteflow',
            name='flow_5',
            field=models.CharField(max_length=1000, verbose_name='时段5'),
        ),
        migrations.AlterField(
            model_name='siteflow',
            name='flow_6',
            field=models.CharField(max_length=1000, verbose_name='时段6'),
        ),
        migrations.AlterField(
            model_name='siteflow',
            name='rate_unit',
            field=models.CharField(default='byte', max_length=10, verbose_name='速率单位'),
        ),
    ]
