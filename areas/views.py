from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CrimeRecord, PoliceDivision
from users.models import User, Review
from django.core.serializers import serialize

# Requests to dispaly html pages

# Iteration 1: (Basic Rendering)
# Map Page
def show_map(request):
    # Iteration 4:
    # PASSSING CRIME RECORDS FROM DB (Codemy.com, 2021)
  
    global locationFilter
    
    # Iteration 4
    # REF: Filtering form Django (Freire, 2019) Youtube Video Playlist
    # REF: Order loaded records by date (ChatGPT,2024) - 'how do i filter records in order of publishDate from newest to oldest'
    review_list = Review.objects.all().order_by('-publishDate')
    police_list = PoliceDivision.objects.all()
    crime_list = CrimeRecord.objects.all()

    sector_like_query = request.GET.get('sector_like')
    policeID_query = request.GET.get('police_ID')
    dropdown_sectors = request.GET.get('dropdown_sectors')

    if is_valid_queryparam(sector_like_query):
        review_list = review_list.filter(policeID__policeName__icontains=sector_like_query)
        crime_list = crime_list.filter(policeID__policeName__icontains=sector_like_query)

    if is_valid_queryparam(policeID_query):
        review_list = review_list.filter(policeID__exact=policeID_query) # check that title contains query that you put in
        crime_list = crime_list.filter(policeID__exact=policeID_query)

    if is_valid_queryparam(dropdown_sectors) and dropdown_sectors != 'Cork (All)':
        review_list = review_list.filter(policeID__policeName__icontains=dropdown_sectors) # check that title contains query that you put in
        crime_list = crime_list.filter(policeID__policeName__icontains=dropdown_sectors)

    context = {
        'review_list' : review_list,
        'police_list' : police_list,
        'crime_list': crime_list
    }

    return render(request, 'map.html', context)             


# Landing Page
def landing_page(request):
    return render(request, 'landing.html') #Iteration 1

# Iteration 4
# Verifying if parameters are valid in policeID search bar (int)
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
        crime_list = crime_list.filter(crimeType__icontains=crime_type_query) # check that title contains query that you put in

    if is_valid_queryparam(policeID_query):
        crime_list = crime_list.filter(policeID__exact=policeID_query) # check that title contains query that you put in

    if is_valid_queryparam(dropdown_sectors) and dropdown_sectors != 'Cork (All)':
        crime_list = crime_list.filter(policeID__policeName__icontains=dropdown_sectors) # check that title contains query that you put in
    
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

    # Iteration 4
    # REF: Filtering form Django (Freire, 2019) Youtube Video Playlist
    sector_like_query = request.GET.get('sector_like')
    policeID_query = request.GET.get('police_ID')
    dropdown_sectors = request.GET.get('dropdown_sectors')

    if is_valid_queryparam(sector_like_query):
        review_list = review_list.filter(policeID__policeName__icontains=sector_like_query)

    if is_valid_queryparam(policeID_query):
        review_list = review_list.filter(policeID__exact=policeID_query) # check that title contains query that you put in

    if is_valid_queryparam(dropdown_sectors) and dropdown_sectors != 'Choose..':
        review_list = review_list.filter(policeID__policeName__icontains=dropdown_sectors) # check that title contains query that you put in
    
    context = {
        'review_list' : review_list,
        'police_list' : police_list

    }
    return render(request, 'map.html', context) # Can now reference crime records from DB in html

"""
REFERENCES:

Iteration 4:
    Codemy.com (2021). Fetch Data From a Database And Output To A Webpage - Django Wednesdays #5. YouTube. Available at: https://www.youtube.com/watch?v=H3joYTIRqKk [Accessed 4 Feb. 2024].
    Freire, M. (2019). Build a dynamic filtering form with Django // 6 - Filtering by date and view count. YouTube. Available at: https://www.youtube.com/watch?v=n1_MQiSXyxw [Accessed 7 Feb. 2024].
    ChatGPT (2024).'how do i filter records in order of publishDate from newest to oldest'
‌


"""