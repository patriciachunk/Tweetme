# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-25 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0009_tweet_liked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='Liked',
            new_name='liked',
        ),
        migrations.AddField(
            model_name='tweet',
            name='Reply',
            field=models.BooleanField(default=False, verbose_name='Is a reply?'),
        ),
    ]
