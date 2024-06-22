from django.urls import path
from .views import ContactViewPage

app_name = "contacts"

urlpatterns = [
    path('contact/', ContactViewPage.as_view(), name="contact"),
]