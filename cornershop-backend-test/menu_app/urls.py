from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'menu_app'

router = DefaultRouter()
router.register(r'users', views.UserviewSet, basename='users')
router.register(r'usersbycountry', views.UsersByCountryViewSet, basename='usersbycountry')
router.register(r'meals', views.MenuViewSet, basename='meals')
router.register(r'menuschedules', views.MenuscheduleViewSet, basename='menuschedules')
router.register(r'usercomments', views.UsersChoices, basename='usercomments')
urlpatterns = router.urls