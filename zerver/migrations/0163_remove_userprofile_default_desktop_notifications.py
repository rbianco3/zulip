# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-28 20:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0162_change_default_community_topic_editing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_desktop_notifications',
        ),
    ]