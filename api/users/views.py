from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests

User = get_user_model()

class GetCityWatherView(APIView):
    """ Get City Weather API """
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        try:
            city = self.request.query_params.get('city')
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city+'&APPID=9173443ab2c336e365088e491039d802', params=request.GET)
            if r.status_code == 200:
                content = r.json()
                return Response(content)
            else:
                content = {'error': 'Sorry we can not reach any data.'}
                return Response(content,status=HTTP_400_BAD_REQUEST)
        except:
            content = {'error': 'Sorry we can not reach any data.'}
            return Response(content,status=HTTP_400_BAD_REQUEST)


class UserCreateAPIView(generics.CreateAPIView):
    """ Create New user endpoint """
    queryset = User.objects.all()
    serializer_class = UserSerializer


""" User login Endpoint """
@csrf_exempt
@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please enter username and password.'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Wrong username or password'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)