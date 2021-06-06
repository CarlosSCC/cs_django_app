from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(primary_key=True, unique=True)
    name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)

    class Meta:
        ordering = ["-email"]


class Menu(models.Model):
    alias = models.CharField(primary_key=True, unique=True, max_length=20)
    meal_name = models.CharField(max_length=50)
    appetizers = models.CharField(max_length=50)
    main_meal = models.CharField(max_length=50) 
    desert = models.CharField(max_length=50)
    salad = models.CharField(max_length=50)


class MenuSchedule(models.Model):
    date = models.DateField(primary_key=True)
    alias = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta: 
        ordering = ["-date"]


class UsersChoice(models.Model):
    date = models.ForeignKey(MenuSchedule, on_delete=models.CASCADE)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    user_comments = models.CharField(max_length=250)