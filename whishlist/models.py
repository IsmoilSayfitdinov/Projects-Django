from django.db import models
from django.contrib.auth.models import User
from products.models import ProductsModels  # Mahsulot modelini import qiling

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductsModels, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
