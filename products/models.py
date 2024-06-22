from django.db import models
from django.contrib.auth.models import User

class AuthorProducstModels(models.Model):
    name = models.CharField(max_length=30, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class CategoryModels(models.Model):
    name = models.CharField(max_length=100)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

# Create your models here.
class ProductsModels(models.Model):
    category = models.ForeignKey(CategoryModels, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products-image/', null=True, verbose_name="name")
    image2 = models.ImageField(upload_to='products-image/', null=True, verbose_name='name')
    image3 = models.ImageField(upload_to='products-image/', null=True, verbose_name='name')
    image4 = models.ImageField(upload_to='products-image/', null=True, verbose_name='name')
    image5 = models.ImageField(upload_to='products-image/', null=True, verbose_name='name')
    name = models.CharField(max_length=100 , verbose_name='name')
    reyting = models.IntegerField(verbose_name='name')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='name')
    info = models.TextField( verbose_name='name')
    description = models.CharField(max_length=100, verbose_name='name')
    discount = models.IntegerField(verbose_name='name')
    
    count = models.IntegerField(verbose_name='name')
    dimension = models.CharField(max_length=100)
    
    author = models.ForeignKey(AuthorProducstModels, on_delete=models.CASCADE, null=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    
    def is_discount(self):
        return self.discount != 0
    
    def math_discount(self):
        if self.is_discount:
            return self.price - self.price * self.discount / 100
        else:
            return self.price
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    

class CommentsProductsModle(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(ProductsModels, on_delete=models.CASCADE, related_name='comments')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.comment} - {self.user} - {self.products}"
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'