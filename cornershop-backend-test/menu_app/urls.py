from django.urls import path

from . import views

app_name = 'menu_app'
urlpatterns = [
    path("users/", views.UserView.as_view(), name="users")
]