from django.shortcuts import render

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

# Create your views here.
class UserView(APIView):
    """Unitary view for User

    Allows C:R:U:D. 
    """
    def get_user(email: str) -> object:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer = UserSerilizer(get_user(email))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, email):
        user = User.objects.get(email=email)

        pass

    def delete(self, request, email):
        user = User.objects.get(email=email)
        user.delete()
        return Response(sresponse)


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
        users = User.objects.filter(country=country)
        users_serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
