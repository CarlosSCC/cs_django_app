from django.urls import path

from . import views

app_name = 'menu_app'
urlpatterns = [
    # individual user fetch, CRUD
    path("user/<str:email>", views.UserView.as_view(), name="user"),
    
    # check if password matches, R
    path("user-auth/<str:email>", views.UserAuth.as_view(), name="user-auth"),

    # get users by country, R
    path("users/<str:country>", views.CountryUsers.as_view() , name="users-country"),

    # get users choice on a date, R 
    #path("users-choice/<str:date>", views.UsersChoice.as_view(), "users-choice"),

]