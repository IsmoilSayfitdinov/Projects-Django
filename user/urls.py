from django.urls import path
from .views import user_login, register, user_logout

app_name = 'users'

urlpatterns=[
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]