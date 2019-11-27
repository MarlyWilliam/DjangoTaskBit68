from django.urls import path
from .views import UserCreateAPIView, login
from rest_framework.authtoken import views

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', UserCreateAPIView.as_view(), name="register")
]