# STD lib

# Thrid-party
from rest_framework import serializers

# Local modules
from .models import User, Menu, UsersChoice, MenuSchedule


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'country']


class MealSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Menu
        fields = [
            'alias', 
            'meal_name', 
            'appetizers', 
            'main_meal',
            'desert',
            'salad'
        ]

class MenuScheduleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MenuSchedule
        fields = ['date', 'alias']


class UserChoicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = UsersChoice
        fields = ['date', 'user', 'user_comments']