# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricehound_admin', '0010_auto_20171029_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlisting',
            name='available',
            field=models.NullBooleanField(editable=False),
        ),
    ]
