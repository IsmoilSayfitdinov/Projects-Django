from django.urls import path
from products.views import ProductsView
from products.views import PageProductsDetailView, add_cart_remove_cart, ShopingCratView
app_name = "products"

urlpatterns = [
    path("products/", ProductsView.as_view(), name="products"),
    path('single-products/<int:pk>/',PageProductsDetailView.as_view(), name='single-products'), 
    path('single-products/cart_add/<int:pk>/', add_cart_remove_cart, name='cart_add'),
    path('cart-sh/', ShopingCratView.as_view(), name='cart'),
    
]