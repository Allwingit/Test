# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricehound_admin', '0012_auto_20171030_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlisting',
            name='product_id',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
