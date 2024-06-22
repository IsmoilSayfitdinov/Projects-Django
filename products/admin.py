from django.contrib import admin
from products.models import ProductsModels, CommentsProductsModle, AuthorProducstModels, CategoryModels


@admin.register(ProductsModels)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
  
  
@admin.register(CategoryModels)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CommentsProductsModle)
class CommentsModleAdmin(admin.ModelAdmin):
    list_display = ['comment', 'created_at', 'updated_at']


@admin.register(AuthorProducstModels)
class AuthorModelsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']