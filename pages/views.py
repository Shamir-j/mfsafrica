from django.http import HttpResponse, request
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    # if request.user.is_authenticated:
    #     print(args, kwargs)
    #     print(request.user)
    #     user = request.user
        # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
        # return render(request, "home.html", {"user":user})
        return render(request, "home.html")


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def register_view(request, *args, **kwargs):
    return render(request, "register.html")

def points_view(request, *args, **kwargs):
    return render(request, "points.html")


def about_view(request, *args, **kwargs):
    # my_context = {
    #     "title": "abc this is about us",
    #     "this_is_true": True,
    #     "my_number": 123,
    #     "my_list": [1313, 4231, 312, "Abc"],
    #     "my_html": "<h1>Hello World</h1>"

    # }
    # return render(request, "about.html", my_context)
    return render(request, "about.html")

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Socail Page</h1>")