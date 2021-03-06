# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-01 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


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
        migrations.CreateModel(
            name='TitleText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleTextText', models.TextField(max_length=160)),
                ('titleTextCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('titleTextUpdatedAt', models.DateTimeField(auto_now=True)),
                ('titleTextTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='title.Title')),
            ],
        ),
    ]
