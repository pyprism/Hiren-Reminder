# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0003_auto_20170527_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]