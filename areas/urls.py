from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



# Setting views/pages
urlpatterns = [
    path('map/', views.show_map, name='map'), # Iteration 1
    #REF: Change landing page (9CV9 HR, 2019)
    path('', views.landing_page, name='landing_page'), # Iteration 1
    path('crime/', views.show_crime, name='crime_page'), # Iteration 1
    path('reviews/average_rating', views.average_rating, name='average_rating'), # Iteration 6
    path('browse_reviews/', views.show_review, name='review_page'), # Iteration 1


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
REFERENCES:

9CV9 HR (2019). How to Set Up Your Homepage with Django - 9cv9 HR and Career Blog | Top Rated by Readers - Medium. [online] Medium. Available at: https://medium.com/@9cv9official/how-to-set-up-your-homepage-with-django-ae21f439c8a3 [Accessed 9 Nov. 2023].

"""