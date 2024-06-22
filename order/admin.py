from django.contrib import admin
from .models import OrderProducts, OrderModel
# Register your models here.
@admin.register(OrderModel)
class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    
@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product_name']
