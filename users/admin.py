from django.contrib import admin
from .models import *

# Iteration 1:
# Registering models for ADMIN SITE
admin.site.register(User) 
admin.site.register(Review) 