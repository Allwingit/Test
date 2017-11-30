from django.contrib import admin
from .models import Store, Category, Brand, ProductModel, ProductVariant, ProductListing

admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductModel)
admin.site.register(ProductVariant)
admin.site.register(ProductListing)