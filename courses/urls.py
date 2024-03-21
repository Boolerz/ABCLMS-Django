from django.urls import path
from .views import home_page

urlpatterns = [

    # Other project-level URL patterns...
    path('',home_page,),
    path(),  # Include app1's URL patterns, these urls map to courses views like we did with the home page.
]