from django.shortcuts import render

from rest_framework import permissions
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class UserView(APIView):

    def get(self, request):
        # get articules from the model
        # serializer = UserSerilizer(Users, many=True)
        # return Response(serializer.data, )
        return Response("status=200")

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

