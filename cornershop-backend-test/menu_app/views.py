from django.shortcuts import render

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

# Create your views here.
class UserView(APIView):

    def get(self, request, email):
        user = User.objects.get(email=email)
        serializer = UserSerilizer(User)
        return Response(serializer.data)

    def post(self, request):
        pass

    def put(self, request, email):
        pass

    def delete(self, request, email):
        pass


class UserAuth(APIView):

    def get(self, request, id):
        # password = request['password']
        # if users(email=email).password = password
        # return 200
        # else 
        # 400
        return Response("status=200")


class CountryUsers(APIView):

    def get(self, request, country):
        # users = User.objects.get(country=country)
        # users_serializer = UserSerializer(users, many=True)
        pass
