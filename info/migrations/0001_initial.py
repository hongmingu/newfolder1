# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 17:10
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
        ('comment', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flowCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('flowUpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BaseProCon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Baseprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('basePro', models.PositiveIntegerField(default=0)),
                ('baseCon', models.PositiveIntegerField(default=0)),
                ('baseStage', models.PositiveIntegerField(default=0)),
                ('baseBlinded', models.SmallIntegerField(default=1)),
                ('profileCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('profileUpdatedAt', models.DateTimeField(auto_now=True)),
                ('base', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Base')),
            ],
        ),
        migrations.CreateModel(
            name='Bridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bridgeCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('bridgeUpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flowCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('flowUpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commentprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('profileCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('profileUpdatedAt', models.DateTimeField(auto_now=True)),
                ('comment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='PostFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flowCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('flowUpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('profileCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('profileUpdatedAt', models.DateTimeField(auto_now=True)),
                ('post', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
        ),
        migrations.CreateModel(
            name='StashFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flowCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('flowUpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StashProCon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stashprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('stashPro', models.PositiveIntegerField(default=0)),
                ('stashCon', models.PositiveIntegerField(default=0)),
                ('stashStage', models.PositiveIntegerField(default=0)),
                ('stashBlinded', models.SmallIntegerField(default=1)),
                ('profileCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('profileUpdatedAt', models.DateTimeField(auto_now=True)),
                ('stash', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stash.Stash')),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('userprofileCalledName', models.TextField(max_length=30)),
                ('userprofileImage', models.ImageField(blank=True, upload_to='')),
                ('userprofileDescription', models.TextField(max_length=100)),
                ('userprofileCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('userprofileUpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='stashprocon',
            name='conStashProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conStash', to='info.Stashprofile'),
        ),
        migrations.AddField(
            model_name='stashprocon',
            name='proStashProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proStash', to='info.Stashprofile'),
        ),
        migrations.AddField(
            model_name='stashprocon',
            name='userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Userprofile'),
        ),
        migrations.AddField(
            model_name='stashflow',
            name='flowedStashProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Stashprofile'),
        ),
        migrations.AddField(
            model_name='stashflow',
            name='flowingUserProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Userprofile'),
        ),
        migrations.AddField(
            model_name='postflow',
            name='flowedPostProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Postprofile'),
        ),
        migrations.AddField(
            model_name='postflow',
            name='flowingUserProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Userprofile'),
        ),
        migrations.AddField(
            model_name='commentflow',
            name='flowedCommentProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Commentprofile'),
        ),
        migrations.AddField(
            model_name='commentflow',
            name='flowingUserProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Userprofile'),
        ),
        migrations.AddField(
            model_name='bridge',
            name='bridgedUserProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bridgedUserProfile', to='info.Userprofile'),
        ),
        migrations.AddField(
            model_name='bridge',
            name='bridgingUserProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bridgingUserProfile', to='info.Userprofile'),
        ),
        migrations.AddField(
            model_name='baseprocon',
            name='conBaseProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conBase', to='info.Stashprofile'),
        ),
        migrations.AddField(
            model_name='baseprocon',
            name='proBaseProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proBase', to='info.Stashprofile'),
        ),
        migrations.AddField(
            model_name='baseprocon',
            name='userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Userprofile'),
        ),
        migrations.AddField(
            model_name='baseflow',
            name='flowedBaseProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Baseprofile'),
        ),
        migrations.AddField(
            model_name='baseflow',
            name='flowingUserProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Userprofile'),
        ),
        migrations.AlterUniqueTogether(
            name='stashprocon',
            unique_together=set([('userProfile', 'proStashProfile'), ('userProfile', 'conStashProfile')]),
        ),
        migrations.AlterUniqueTogether(
            name='stashflow',
            unique_together=set([('flowingUserProfile', 'flowedStashProfile')]),
        ),
        migrations.AlterUniqueTogether(
            name='postflow',
            unique_together=set([('flowingUserProfile', 'flowedPostProfile')]),
        ),
        migrations.AlterUniqueTogether(
            name='commentflow',
            unique_together=set([('flowingUserProfile', 'flowedCommentProfile')]),
        ),
        migrations.AlterUniqueTogether(
            name='bridge',
            unique_together=set([('bridgingUserProfile', 'bridgedUserProfile')]),
        ),
        migrations.AlterUniqueTogether(
            name='baseprocon',
            unique_together=set([('userProfile', 'proBaseProfile'), ('userProfile', 'conBaseProfile')]),
        ),
        migrations.AlterUniqueTogether(
            name='baseflow',
            unique_together=set([('flowingUserProfile', 'flowedBaseProfile')]),
        ),
    ]
