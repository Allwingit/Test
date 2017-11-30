# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from pricehound_admin.models import ProductListing

class PriceHistory(models.Model):

    listing = models.ForeignKey(ProductListing, on_delete=models.CASCADE)
    price = models.CharField(max_length = 20)
    timestamp = models.DateTimeField(auto_now_add=True)


# Create your models here.
