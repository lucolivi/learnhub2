# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-27 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20161027_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200, unique=True)),
                ('thumbnailUrl', models.CharField(max_length=200)),
                ('level', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Coursee',
        ),
    ]
