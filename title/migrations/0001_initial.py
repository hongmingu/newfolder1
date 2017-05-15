# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleJudgingText', models.TextField(max_length=160, unique=True)),
                ('titleText', models.TextField(max_length=160)),
                ('titleCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('titleUpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]