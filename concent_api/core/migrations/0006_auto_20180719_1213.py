# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-19 12:13
from __future__ import unicode_literals

from django.db import migrations, models
from common.helpers import deserialize_message
from common.helpers import parse_timestamp_to_utc_datetime


def populate_subtask_size_field(apps, _schema_editor):
    Subtask = apps.get_model('core', 'Subtask')
    for subtask in Subtask.objects.all():
        subtask.result_package_size = deserialize_message(subtask.report_computed_task.data).size
        subtask.full_clean()
        subtask.save()


def populate_subtask_deadline_field(apps, _schema_editor):
    Subtask = apps.get_model('core', 'Subtask')
    for subtask in Subtask.objects.all():
        subtask.computation_deadline = parse_timestamp_to_utc_datetime(
            deserialize_message(
                subtask.task_to_compute.data
            ).compute_task_def['deadline']
        )
        subtask.full_clean()
        subtask.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180717_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='computation_deadline',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subtask',
            name='result_package_size',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=False,
        ),
        migrations.RunPython(populate_subtask_size_field),
        migrations.RunPython(populate_subtask_deadline_field),

    ]
