from django.db import models
from django.contrib.auth import get_user_model
from products.models import ProductsModels
# Create your views here.

UserModel = get_user_model()

class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'  


class OrderProducts(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(ProductsModels, on_delete=models.SET_NULL, related_name="orders", null=True)
    product_name = models.CharField(max_length=255)
    count = models.IntegerField()
    dimension = models.CharField(max_length=255)
    price = models.IntegerField()
    info = models.TextField()
    image = models.ImageField(upload_to='order-image/')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.order} - {self.product}"
    
    class Meta:
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProducts'
    