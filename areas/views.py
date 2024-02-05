from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CrimeRecord
from django.core.serializers import serialize

# Requests to dispaly html pages

# Iteration 1: (Basic Rendering)
# Map Page
def show_map(request):
    # Iteration 4:
    # PASSSING CRIME RECORDS FROM DB (Codemy.com, 2021)


    crime_list = CrimeRecord.objects.all()
    

    return render(request, 'map.html',              
        {'crime_list': crime_list}) # Can now reference crime records from DB in map.html




# Landing Page
def landing_page(request):
    return render(request, 'landing.html') #Iteration 1


"""
REFERENCES:

Iteration 4:
    Codemy.com (2021). Fetch Data From a Database And Output To A Webpage - Django Wednesdays #5. YouTube. Available at: https://www.youtube.com/watch?v=H3joYTIRqKk [Accessed 4 Feb. 2024].



"""