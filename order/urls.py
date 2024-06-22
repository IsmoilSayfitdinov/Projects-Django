from django.urls import path

from .views import CheackOutView, orders_view

app_name = 'orders'

urlpatterns = [
        path('cheackout/', CheackOutView.as_view(), name='cheackout'),
        path('orders/', orders_view, name='orders'),
]