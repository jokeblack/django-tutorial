# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-18 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'profile_image'),
        ),
    ]