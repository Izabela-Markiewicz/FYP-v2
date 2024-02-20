"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Iteration 1
    path('', include('users.urls')), # Environment
    path('', include('areas.urls')), # Iteration 1
    path('users/', include('django.contrib.auth.urls')), # Iteration 5 (Codemy.com, 2021)
     
]

# Setting directory for 'static' folder for images, css, js, etc.
#REF: Iteration1-1(ChatGPT3.5,2023)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Iteration 1


"""
REFERENCES:
Iteration 1:   
    ChatGPT, 2023. Iteration1-1. Prompt- "my static file is a folder in my overall django project. i used a bootstrap template for one of my apps, but the css or images wont load"

Iteration 2:
    Codemy.com (2021). Login With User Authentication - Django Wednesdays #21. YouTube. Available at: https://www.youtube.com/watch?v=CTrVDi3tt8o [Accessed 19 Feb. 2024].

‌
"""