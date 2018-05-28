# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primesession', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionID', models.CharField(max_length=30, unique=True)),
                ('token', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
