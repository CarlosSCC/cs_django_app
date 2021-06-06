from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)


class Menu(models.Model):
    alias = models.CharField(primary_key=True, unique=True, max_length=20)
    nombre = models.CharField(max_length = 50)
    entrada = models.CharField(max_length = 50)
    plato_fuerte = models.CharField(max_length = 50) 
    postre = models.CharField(max_length = 50)
    ensalada = models.CharField(max_length = 50)


class Calendar(models.Model):
    date = models.DateField(primary_key=True, unique=True)
    day = models.CharField(max_length = 50)
    month = models.CharField(max_length = 50)
    year = models.CharField(max_length = 50)


class UsersChoice(models.Model):
    menu_name = models.ForeignKey(Menu, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    user_comments = models.CharField(max_length = 250)
    date = models.ForeignKey(Calendar, on_delete=models.PROTECT)


class MenuSchedule(models.Model):
    date = models.ForeignKey(Calendar, on_delete=models.PROTECT)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)

