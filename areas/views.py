from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CrimeRecord

# Requests to dispaly html pages


# Map Page
def show_map(request):
    # Iteration 3:

    # Calculation Testing:
    CrimeAvg = 46+3

    # Define your variable here
    my_variable = int(CrimeAvg)

    print(my_variable)  # Check in the console

    # Pass the variable to the template context
    context = {'my_variable': my_variable}

    # Iteration 1:
    return render(request, 'map.html', context) 


# Landing Page
def landing_page(request):
    return render(request, 'landing.html') #Iteration 1


"""
REFERENCES:


"""