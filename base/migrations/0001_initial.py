# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 17:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('title', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseSlug', models.SlugField(unique=True)),
                ('baseText', models.TextField(max_length=100)),
                ('baseCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('baseUpdatedAt', models.DateTimeField(auto_now=True)),
                ('baseTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='title.Title')),
                ('baseUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]