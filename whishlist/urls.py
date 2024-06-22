from django.urls import path
from .views import AddToWishlistView, RemoveFromWishlistView, ViewWishlist

app_name = 'whishlist'

urlpatterns = [
    path('add/<int:pk>/', AddToWishlistView.as_view(), name='add_to_wishlist'),
    path('remove/<int:pk>/', RemoveFromWishlistView.as_view(), name='remove_from_wishlist'),
    path('wishlist/', ViewWishlist.as_view(), name='view_wishlist'),
]
