from django.contrib import admin

# Register your models here.
from .models import Product, Order, UOM, OrderDetail

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UOM)
admin.site.register(OrderDetail)