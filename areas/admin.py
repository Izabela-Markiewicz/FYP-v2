from django.contrib import admin
from .models import *
from . import models
from import_export.admin import ImportExportModelAdmin # Upload CSVs to Django Admin



# Register your models here.
admin.site.register(Gradient)
admin.site.register(Area)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(PoliceDivision)
admin.site.register(CrimeRecord)


"""
FOR FUTURE ITERATION

# Admin Upload to DB using CSV
#REF: Django Import Export (The Proton Guy, 2023)
class CrimeRecordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(models.CrimeRecord, CrimeRecordAdmin)
"""


"""
REFERENCES:
THE PROTON GUY (2022). Django Import Export | Import And Export Data To & From Database. YouTube. Available at: https://www.youtube.com/watch?v=DIr1wYjTM64 [Accessed 8 Nov. 2023].



"""