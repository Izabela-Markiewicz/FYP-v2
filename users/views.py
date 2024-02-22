from django.shortcuts import render, redirect
from rest_framework import generics
from .models import User, Review
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout # Iteration 5
from django.contrib import messages # Iteration 5
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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
# REF: Django Login and User Authentication [Youtube] (Codemy.com, 2021)
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

# Iteration 5
# Logout
# REF: Log Out With User Authentication [Youtube] (Codemy.com, 2021)
def logout_user(request):
    logout(request)
    messages.success(request, ("You are now logged out."))
    return redirect('landing_page')

# Iteration 5
# Register User
# REF: How To Register Users [Youtube] (Codemy.com, 2021)
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('landing_page') 
    else:
        form = RegisterUserForm()

    return render(request,'register.html', {
        'form' : form,
    })

# Iteration 5
# Create Review
# REF: How To Add Database Forms To A Web Pages [Youtube] (Codemy.com, 2021)
def add_review(request):
    submitted = False
    if request.method == "POST":
        form = ReviewForm(request.POST)
        # REF: Add Venue Owner [Youtube] (Codemy.com, 2021)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user.id # passing logged in user ID to review
            review.owner = request.user
          #  review.userID = review.author
           # user_instance = User.objects.get(pk=request.user.pk)
           # review.userID = user_instance  # Assign the User instance
            review.save()
           #  return HttpResponseRedirect('/add_review?submitted=True')
            return redirect(reverse('add_review') + '?submitted=True')
    else:
        form = ReviewForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_review.html', {
        'form' : form,
        'submitted' : submitted,
        })

"""
REFERENCES:

Environment:
    MrNick. “Building a CRUD API with Django Rest Framework and PostgreSQL - Tutorial for Beginners.” Www.youtube.com, Feb. 2023, www.youtube.com/watch?v=1YmfnQ8i9o8. Accessed 23 Oct. 2023.

Iteration 5:
    Codemy.com (2021). Login With User Authentication - Django Wednesdays #21. YouTube. Available at: https://www.youtube.com/watch?v=CTrVDi3tt8o [Accessed 20 Feb. 2024].
    Codemy.com (2021). Log Out With User Authentication - Django Wednesdays #22. YouTube. Available at: https://www.youtube.com/watch?v=BTq0MAIJEH8&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=23 [Accessed 21 Feb. 2024].
    Codemy.com (2021). How To Register Users - Django Wednesdays #24. YouTube. Available at: https://www.youtube.com/watch?v=EqjRhO5CK6A&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=25 [Accessed 21 Feb. 2024].
    Codemy.com (2021). How To Add Database Forms To A Web Page - Django Wednesdays #7. YouTube. Available at: https://www.youtube.com/watch?v=CVEKe39VFu8&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=7 [Accessed 21 Feb. 2024].
    Codemy.com (2021). Add Venue Owner - Django Wednesdays #29. YouTube. Available at: https://www.youtube.com/watch?v=fXKLLwdryHQ&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=29 [Accessed 22 Feb. 2024].

‌
‌
‌
‌
‌

"""    