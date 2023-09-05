from django.contrib import admin
from .models import Product, Location, ProductMovement, ProductLocation

# Register your models here.

admin.site.register(Product)
admin.site.register(Location)
admin.site.register(ProductMovement)
admin.site.register(ProductLocation)
