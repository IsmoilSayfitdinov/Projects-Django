from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Wishlist
from products.models import ProductsModels

class AddToWishlistView(View):
    def get(self, request, pk):
        product = get_object_or_404(ProductsModels, id=pk)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
        if created:
            message = "Mahsulot wishlist-ga qo'shildi."
        else:
            message = "Mahsulot allaqachon wishlist-da mavjud."
        return redirect('whishlist:view_wishlist')

class RemoveFromWishlistView(View):
    def get(self, request, pk):
        product = get_object_or_404(ProductsModels, id=pk)
        wishlist = Wishlist.objects.filter(user=request.user, product=product)
        if wishlist.exists():
            wishlist.delete()
            message = "Mahsulot wishlist-dan olib tashlandi."
        else:
            message = "Mahsulot wishlist-da topilmadi."
        return redirect('whishlist:view_wishlist')

class ViewWishlist(View):
    def get(self, request):
        wishlist_items = Wishlist.objects.filter(user=request.user)
        return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})