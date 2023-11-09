from django.shortcuts import render
from django.http import HttpResponse

# Requests to dispaly html pages


# Map Page
def show_map(request):
    return render(request, 'map.html') # Iteration 1

# Landing Page
def landing_page(request):
    return render(request, 'landing.html') #Iteration 1


"""
REFERENCES:


"""