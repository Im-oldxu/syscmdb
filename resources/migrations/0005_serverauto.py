# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-09-25 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_auto_20190923_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_inner', models.CharField(max_length=32, unique=True, verbose_name='连接IP地址')),
                ('port', models.IntegerField(verbose_name='连接端口')),
                ('os_status', models.IntegerField(choices=[(0, 'Linux'), (1, 'Windows'), (2, 'Mac')], verbose_name='操作系统')),
                ('system_status', models.IntegerField(choices=[(0, '虚拟机'), (1, '物理机')], verbose_name='机器类型')),
            ],
            options={
                'default_permissions': [],
            },
        ),
    ]
