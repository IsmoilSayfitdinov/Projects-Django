from django.urls import path
from blogs.views import BlogListView,BlogDeatilView

app_name = "blogs"

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name="blogs"),
    path('blog-details/<int:pk>/', BlogDeatilView.as_view(), name="blog_details"),
]