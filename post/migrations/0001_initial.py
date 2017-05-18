# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-18 13:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('title', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postText', models.TextField(max_length=2000)),
                ('postCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('postUpdatedAt', models.DateTimeField(auto_now=True)),
                ('postTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='title.Title')),
                ('postUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postTextText', models.TextField(max_length=2000)),
                ('postTextCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('postTextUpdatedAt', models.DateTimeField(auto_now=True)),
                ('postTextPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
        ),
    ]
