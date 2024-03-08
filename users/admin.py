from django.contrib import admin
from .models import *

# Iteration 1:
# Registering models for ADMIN SITE
admin.site.register(User) 
admin.site.register(Review) 


# Iteration 6:
# Show Reviews Pending Approval in Admin
# REF: GitHub Copilt (2024) - 'i want to add to the admin view an option to 'View Reviews Pending Approval'. jsut as admin site loads all Review onjects, i want a place where it does the same thing, but only loads those where Review.approved == False
class UnapprovedReview(Review):
    class Meta:
        proxy = True
        verbose_name = 'Reviews Pending Approval'
        verbose_name_plural = 'Reviews Pending Approval'

class UnapprovedReviewAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(approved=False)

    
admin.site.register(UnapprovedReview, UnapprovedReviewAdmin)
    

"""
REFERENCES:

Iteration 6: 
    GitHub Copilt (2024) - 'i want to add to the admin view an option to 'View Reviews Pending Approval'. jsut as admin site loads all Review onjects, i want a place where it does the same thing, but only loads those where Review.approved == False





"""