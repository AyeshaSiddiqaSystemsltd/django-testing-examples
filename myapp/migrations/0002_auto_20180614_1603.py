# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyNullableOtherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='mymodel',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='nullable_other',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.MyNullableOtherModel'),
        ),
    ]