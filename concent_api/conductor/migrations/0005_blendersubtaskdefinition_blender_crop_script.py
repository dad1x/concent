# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-04 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conductor', '0004_auto_20180704_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='blendersubtaskdefinition',
            name='blender_crop_script',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]