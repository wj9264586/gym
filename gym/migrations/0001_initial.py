# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-03 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_time', models.DateTimeField(auto_created=True)),
                ('equipment_name', models.CharField(max_length=255)),
                ('equipment_number', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='器材编号')),
                ('repair_time', models.DateTimeField(null=True)),
                ('equipment_status', models.IntegerField(choices=[(1, '良好'), (2, '已损坏'), (3, '已维修'), (4, '已报废')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MemberCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.IntegerField(choices=[(1, '10次卡'), (2, '月卡'), (3, '季卡'), (4, '半年卡'), (5, '年卡')], verbose_name='会员卡类型')),
                ('is_active', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('use_time', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('phone', models.CharField(db_index=True, max_length=11, unique=True, verbose_name='手机号')),
                ('password', models.CharField(default='000000', max_length=255)),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('id_card', models.CharField(max_length=18)),
                ('portrait', models.ImageField(max_length=255, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='StaffManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=11, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=255)),
                ('role', models.IntegerField(choices=[(1, '前台'), (2, '后勤'), (3, '人事')], verbose_name='用户角色')),
                ('authority', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StaffUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='姓名')),
                ('number', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='工号')),
                ('phone', models.CharField(max_length=11)),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('age', models.IntegerField()),
                ('department', models.IntegerField(choices=[(1, '营销部'), (2, '行政部'), (3, '人事部'), (4, '后勤部'), (5, '财务部')], verbose_name='所属部门')),
                ('monthly_pay', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='memberinfo',
            name='transactor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.StaffUserInfo'),
        ),
        migrations.AddField(
            model_name='membercard',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.MemberInfo'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='buy_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.StaffUserInfo'),
        ),
    ]