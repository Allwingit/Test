# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricehound_admin', '0013_productlisting_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlisting',
            name='listing_url',
            field=models.URLField(blank=True, unique=True),
        ),
    ]
