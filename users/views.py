from django.shortcuts import render, redirect
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout # Iteration 5
from django.contrib import messages # Iteration 5

# Create your views here.

# Environment
# Create a user and display info
# REF: CRUD with REST APIs (MrNick, 2023)
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Environment
# Retrieve, Update or Delete user by ID
# REF: CRUD with REST APIs (MrNick, 2023)
class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Iteration 5
# Login / Authenticate
# REF: Django Login nad User Authentication [Youtube] (Codemy.com, 2021)
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')       
        else:
            messages.success(request, ("There was an error loggin in, please try again."))
            return redirect('login_user')
        
    else: 
        return render(request, 'login.html', {})


"""
REFERENCES:

Environment:
    MrNick. “Building a CRUD API with Django Rest Framework and PostgreSQL - Tutorial for Beginners.” Www.youtube.com, Feb. 2023, www.youtube.com/watch?v=1YmfnQ8i9o8. Accessed 23 Oct. 2023.

Iteration 5:
    Codemy.com (2021). Login With User Authentication - Django Wednesdays #21. YouTube. Available at: https://www.youtube.com/watch?v=CTrVDi3tt8o [Accessed 20 Feb. 2024].

‌

"""    