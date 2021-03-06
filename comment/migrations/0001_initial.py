# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-01 10:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stash', '0001_initial'),
        ('base', '0001_initial'),
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.TextField(max_length=200)),
                ('commentCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('commentUpdatedAt', models.DateTimeField(auto_now=True)),
                ('commentBase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Base')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentBaseText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentBaseTextCommentText', models.TextField(max_length=200)),
                ('commentBaseTextCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('commentBaseTextUpdatedAt', models.DateTimeField(auto_now=True)),
                ('commentBaseTextCommentBase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.CommentBase')),
            ],
        ),
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.TextField(max_length=200)),
                ('commentCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('commentUpdatedAt', models.DateTimeField(auto_now=True)),
                ('commentPost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentPostText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentPostTextCommentText', models.TextField(max_length=200)),
                ('commentPostTextCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('commentPostTextUpdatedAt', models.DateTimeField(auto_now=True)),
                ('commentPostTextCommentStash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.CommentPost')),
            ],
        ),
        migrations.CreateModel(
            name='CommentStash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.TextField(max_length=200)),
                ('commentCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('commentUpdatedAt', models.DateTimeField(auto_now=True)),
                ('commentStash', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stash.Stash')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentStashText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentStashTextCommentText', models.TextField(max_length=200)),
                ('commentStashTextCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('commentStashTextUpdatedAt', models.DateTimeField(auto_now=True)),
                ('commentStashTextCommentStash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.CommentStash')),
            ],
        ),
    ]
