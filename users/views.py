from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# Create your views here.

# Create a user and display info
# REF: CRUD with REST APIs (MrNick, 2023)
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Retrieve, Update or Delete user by ID
# REF: CRUD with REST APIs (MrNick, 2023)
class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




"""
REFERENCES:

MrNick. “Building a CRUD API with Django Rest Framework and PostgreSQL - Tutorial for Beginners.” Www.youtube.com, Feb. 2023, www.youtube.com/watch?v=1YmfnQ8i9o8. Accessed 23 Oct. 2023.


"""    