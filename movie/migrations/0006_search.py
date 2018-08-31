# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20170412_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=30)),
                ('times', models.IntegerField(default=0)),
            ],
        ),
    ]
