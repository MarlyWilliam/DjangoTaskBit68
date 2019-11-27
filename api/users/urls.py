from django.urls import path
from .views import login
from rest_framework.authtoken import views

urlpatterns = [
    path('login/', login, name="login")
]