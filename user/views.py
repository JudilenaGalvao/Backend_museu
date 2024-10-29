from django.shortcuts import render
from rest_framework import viewsets
from user.models import User
from user.serializers import UserSerializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
    
