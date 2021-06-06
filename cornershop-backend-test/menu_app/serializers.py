# STD lib

# Thrid-party
from rest_framework import serializers

# Local modules
from models import User, Menu, UsersChoice


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'country']


class MealSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Menu
        field = []


class UserChoicesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UsersChoice
        fields = []