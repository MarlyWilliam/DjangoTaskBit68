from django.urls import path
from .views import UserCreateAPIView, login, GetCityWatherView
from rest_framework.authtoken import views

urlpatterns = [
    path('user/login/', login, name="login"),
    path('user/register/', UserCreateAPIView.as_view(), name="register"),
    path('weather/', GetCityWatherView.as_view(), name="get-city-weather")
]