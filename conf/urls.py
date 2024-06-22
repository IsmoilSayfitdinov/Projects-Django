from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace="pages")),
    path('', include("blogs.urls", namespace="blogs")),
    path('', include("products.urls", namespace="products")),
    path('', include("contacts.urls", namespace="contacts")),
    path('', include("user.urls", namespace="users")),
    path('', include("order.urls", namespace="orders")),
    path('', include("whishlist.urls", namespace="whishlist")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)