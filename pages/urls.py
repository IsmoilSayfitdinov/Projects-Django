from .views import HomePageView, search, About
from django.urls import path
app_name = "pages"

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('search/', search, name='search_data'),
    path('about/' , About.as_view(), name="about"),
]