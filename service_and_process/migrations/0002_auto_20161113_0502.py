# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-12 23:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_and_process', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='masterattribute',
            old_name='type',
            new_name='attribute_type',
        ),
        migrations.AlterUniqueTogether(
            name='masterattribute',
            unique_together=set([('label', 'attribute_type')]),
        ),
    ]
