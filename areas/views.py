from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CrimeRecord, PoliceDivision
from users.models import User, Review
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.db.models import Avg
from django.shortcuts import get_object_or_404
import random
import os
from django.conf import settings

# Requests to dispaly html pages

# Iteration 1: (Basic Rendering)
# Map Page
def show_map(request):
    # Iteration 4:
    # PASSSING CRIME RECORDS FROM DB 
    # REF: Fetch data from DB and ouput on webpage (Codemy.com, 2021)
    # REF: Filtering form Django (Freire, 2019) Youtube Video Playlist
    # REF: Order loaded records by date (ChatGPT,2024) - 'how do i filter records in order of publishDate from newest to oldest'
    review_list = Review.objects.all().order_by('-publishDate') # Order by most recent review
    police_list = PoliceDivision.objects.all()
    crime_list = CrimeRecord.objects.all()

    # Get value of form controls as a parameter
    sector_like_query = request.GET.get('sector_like') 
    policeID_query = request.GET.get('police_ID')
    dropdown_sectors = request.GET.get('dropdown_sectors')

    # Fetch all records similar to input, doesn't have to be exact/complete   
    if is_valid_queryparam(sector_like_query):
        review_list = review_list.filter(policeID__policeName__icontains=sector_like_query) 
        crime_list = crime_list.filter(policeID__policeName__icontains=sector_like_query)

    # ID search needs to exactly match  
    if is_valid_queryparam(policeID_query):
        review_list = review_list.filter(policeID__exact=policeID_query) 
        crime_list = crime_list.filter(policeID__exact=policeID_query)

    # Dropdown
    if is_valid_queryparam(dropdown_sectors) and dropdown_sectors != 'Cork (All)': 
        review_list = review_list.filter(policeID__policeName__icontains=dropdown_sectors)
        crime_list = crime_list.filter(policeID__policeName__icontains=dropdown_sectors)


    # Iteration 6:
    # AVG User Reviews
    #approved_reviews = Review.objects.filter(approved=True)
    #avg_rating = approved_reviews.aggregate(Avg('feelRating'))['feelRating__avg']
    location_filter = request.GET.get('locationFilter')
    if location_filter and Review.objects.filter(policeID=location_filter).exists():
        avg_rating = Review.objects.filter(policeID=location_filter).aggregate(Avg('feelRating'))['feelRating__avg']
    else:
        avg_rating = Review.objects.filter(approved=True).aggregate(Avg('feelRating'))['feelRating__avg']

    approved_reviews_count = Review.objects.filter(approved=True).count()

   
    context = {
        'review_list' : review_list,
        'police_list' : police_list,
        'crime_list': crime_list,
        'avg_rating' : avg_rating,
        'locationFilter': location_filter,
        'approved_reviews_count': approved_reviews_count,
        
    }
          
    return render(request, 'map.html', context)             

def average_rating(request):
    # Get the locationFilter query parameter
    locationFilter = request.GET.get('locationFilter')

    # Query the Review model
    reviews = Review.objects.filter(policeID=locationFilter)

    # Calculate the average feelRating
    averageRating = reviews.aggregate(Avg('feelRating'))['feelRating__avg']

    # Return the average rating as JSON
    return JsonResponse({'averageRating': averageRating})

# Landing Page
def landing_page(request):
    return render(request, 'landing.html') #Iteration 1

# Iteration 4
# Verifying if parameters are valid type eg int
def is_valid_queryparam(param):
     return param != '' and param is not None # boolean check ture/false

def show_crime(request):
    # Iteration 4:
    # PASSSING CRIME RECORDS FROM DB (Codemy.com, 2021)
    crime_list = CrimeRecord.objects.all()
    police_list = PoliceDivision.objects.all()

    global locationFilter

    # Iteration 4
    # REF: Filtering form Django (Freire, 2019) Youtube Video Playlist
    sector_like_query = request.GET.get('sector_like')
    crime_type_query = request.GET.get('crime_type')
    policeID_query = request.GET.get('police_ID')
    dropdown_sectors = request.GET.get('dropdown_sectors')

    if is_valid_queryparam(sector_like_query):
        crime_list = crime_list.filter(policeID__policeName__icontains=sector_like_query)

    if is_valid_queryparam(crime_type_query):
        crime_list = crime_list.filter(crimeType__icontains=crime_type_query)

    if is_valid_queryparam(policeID_query):
        crime_list = crime_list.filter(policeID__exact=policeID_query) 

    if is_valid_queryparam(dropdown_sectors) and dropdown_sectors != 'Cork (All)':
        crime_list = crime_list.filter(policeID__policeName__icontains=dropdown_sectors) 
    
    context = {
        'crime_list' : crime_list,
        'police_list' : police_list

    }
    return render(request, 'crime_stats.html', context) # Can now reference crime records from DB in html

def show_reviews(request):
    # Iteration 4:
    # PASSSING CRIME RECORDS FROM DB (Codemy.com, 2021)
    review_list = Review.objects.all()
    police_list = PoliceDivision.objects.all()

    global locationFilter

    # Iteration 4:
    # REF: Filtering form Django (Freire, 2019) Youtube Video Playlist
    sector_like_query = request.GET.get('sector_like')
    policeID_query = request.GET.get('police_ID')
    dropdown_sectors = request.GET.get('dropdown_sectors')

    if is_valid_queryparam(sector_like_query):
        review_list = review_list.filter(policeID__policeName__icontains=sector_like_query)

    if is_valid_queryparam(policeID_query):
        review_list = review_list.filter(policeID__exact=policeID_query)

    if is_valid_queryparam(dropdown_sectors) and dropdown_sectors != 'Cork (All)':
        review_list = review_list.filter(policeID__policeName__icontains=dropdown_sectors) 
    

    # Iteration 5:
    # Update record 
    review_owner = User.objects.get(pk=Review.owner)
    context = {
        'review_list' : review_list,
        'police_list' : police_list,

    }
    return render(request, 'reviews.html', context) # Can now reference crime records from DB in html

# Iteration 6:
def show_review(request):
    locationFilter = request.GET.get('locationFilter')

    if locationFilter:
        review_filtered = Review.objects.filter(policeID=locationFilter).order_by('-publishDate')
        police_division = get_object_or_404(PoliceDivision, policeID=locationFilter)
        avg_rating = Review.objects.filter(policeID=locationFilter).aggregate(Avg('feelRating'))['feelRating__avg']
        count_reviews = Review.objects.filter(policeID=locationFilter).count()

    else:
        review_filtered = Review.objects.all().order_by('-publishDate')
        police_division = None

    police_list = PoliceDivision.objects.all()

    context = {
        'review_filtered': review_filtered,
        'police_list': police_list,
        'police_division': police_division,
        'avg_rating': avg_rating,
        'count_reviews': count_reviews,
    }
    return render(request, 'reviews.html', context)
"""
REFERENCES:

Iteration 4:
    Codemy.com (2021). Fetch Data From a Database And Output To A Webpage - Django Wednesdays #5. YouTube. Available at: https://www.youtube.com/watch?v=H3joYTIRqKk [Accessed 4 Feb. 2024].
    Freire, M. (2019). Build a dynamic filtering form with Django // 6 - Filtering by date and view count. YouTube. Available at: https://www.youtube.com/watch?v=n1_MQiSXyxw [Accessed 7 Feb. 2024].
    ChatGPT (2024).'how do i filter records in order of publishDate from newest to oldest'
‌


"""