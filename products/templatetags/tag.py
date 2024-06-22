from django import template
from products.models import ProductsModels

register = template.Library()


@register.filter
def add_cart_products(request):
    cart = request.session.get('cart', [])
    products = ProductsModels.objects.filter(pk__in = cart)
    
    return products