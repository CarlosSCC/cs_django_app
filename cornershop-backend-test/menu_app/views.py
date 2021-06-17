from rest_framework import permissions, status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .serializers import UserSerializer, MealSerializer, MenuScheduleSerializer, UserChoicesSerializer
from .models import User, Menu, MenuSchedule, UsersChoice


class UserviewSet(viewsets.ModelViewSet):
    """

    """
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.all()
        serializer =  UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 


class  UsersByCountryViewSet(viewsets.ViewSet):
    """
    Simple ViewSet for displaying users from an specific 
    country
    """
    def list(self, request):
        queryset = User.filter(country=request.kwargs['country'])
        serializer =  UserSerializer(queryset, many=True)
        return Response(serializer.data)


class MenuViewSet(viewsets.ModelViewSet):
    """

    """
    serializer_class = MealSerializer

    def list(self, request):
        queryset = Menu.objects.all()
        serializer =  MealSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuscheduleViewSet(viewsets.ModelViewSet):
    """

    """
    serializer_class = MenuScheduleSerializer


    def list(self, request):
        queryset = MenuSchedule.objects.all()
        serializer =  MenuScheduleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MenuScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersChoices(viewsets.ModelViewSet):
    """

    """
    serializer_class = UserChoicesSerializer

    def list(self, request):
        queryset = UsersChoice.objects.all()
        serializer =  UserChoicesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserChoicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    