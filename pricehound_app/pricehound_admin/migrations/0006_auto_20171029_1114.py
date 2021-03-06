# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricehound_admin', '0005_auto_20171029_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlisting',
            name='affiliate_url',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='productlisting',
            name='current_price',
            field=models.CharField(blank=True, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='specifications',
            field=models.TextField(blank=True),
        ),
    ]
