from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Map Page
def show_map(request):
    return render(request, 'map.html')

# Landing Page
def landing_page(request):
    return render(request, 'landing.html')

"""
REFERENCES:


"""