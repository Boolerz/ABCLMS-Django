from django.shortcuts import render
def home_page(request):
    return render(request, "courses/home.html")


# create more views for your courses app and remember to map them in your courses urls.py file