from django.urls import path
from . import views

# Setting views/pages
urlpatterns = [
    path('map/', views.show_map), # Iteration 1
    #REF: Change landing page (9CV9 HR, 2019)
    path('', views.landing_page, name='landing_page') # Iteration 1
]

"""
REFERENCES:

9CV9 HR (2019). How to Set Up Your Homepage with Django - 9cv9 HR and Career Blog | Top Rated by Readers - Medium. [online] Medium. Available at: https://medium.com/@9cv9official/how-to-set-up-your-homepage-with-django-ae21f439c8a3 [Accessed 9 Nov. 2023].

"""