# Generated by Django 3.1 on 2021-04-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HUAWEI', '0008_auto_20210410_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentflow',
            name='flow_1',
            field=models.IntegerField(default=0, verbose_name='时段1'),
        ),
        migrations.AddField(
            model_name='equipmentflow',
            name='flow_2',
            field=models.IntegerField(default=0, verbose_name='时段2'),
        ),
        migrations.AddField(
            model_name='equipmentflow',
            name='flow_3',
            field=models.IntegerField(default=0, verbose_name='时段3'),
        ),
        migrations.AddField(
            model_name='equipmentflow',
            name='flow_4',
            field=models.IntegerField(default=0, verbose_name='时段4'),
        ),
        migrations.AddField(
            model_name='equipmentflow',
            name='flow_5',
            field=models.IntegerField(default=0, verbose_name='时段5'),
        ),
        migrations.AddField(
            model_name='equipmentflow',
            name='flow_6',
            field=models.IntegerField(default=0, verbose_name='时段6'),
        ),
        migrations.AddField(
            model_name='equipmentflow',
            name='total_flow',
            field=models.IntegerField(default=0, verbose_name='总流量'),
        ),
        migrations.AddField(
            model_name='siteflow',
            name='flow_1',
            field=models.IntegerField(default=0, verbose_name='时段1'),
        ),
        migrations.AddField(
            model_name='siteflow',
            name='flow_2',
            field=models.IntegerField(default=0, verbose_name='时段2'),
        ),
        migrations.AddField(
            model_name='siteflow',
            name='flow_3',
            field=models.IntegerField(default=0, verbose_name='时段3'),
        ),
        migrations.AddField(
            model_name='siteflow',
            name='flow_4',
            field=models.IntegerField(default=0, verbose_name='时段4'),
        ),
        migrations.AddField(
            model_name='siteflow',
            name='flow_5',
            field=models.IntegerField(default=0, verbose_name='时段5'),
        ),
        migrations.AddField(
            model_name='siteflow',
            name='flow_6',
            field=models.IntegerField(default=0, verbose_name='时段6'),
        ),
        migrations.AddField(
            model_name='siteflow',
            name='total_flow',
            field=models.IntegerField(default=0, verbose_name='总流量'),
        ),
    ]