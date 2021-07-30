from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
# Create your views here.


# def point_list_view(request):
#     # queryset = Product.objects.all() # list of objects
#     # context = {
#     #     "object_list": queryset
#     # }
#     # return render(request, "points_list.html")

# def homes(request):
#     print(request)
#     response=request.GET.get('http://127.0.0.1:8000/api-auth/points')

#     print(response)
#     return render(request, 'home.html', {'response':response})


def points_list(request):
    response = requests.get('http://127.0.0.1:8000/api-auth/points/')
    points = response.json()
    print(points)
    return render(request, "points_list.html")

def create_point(request):
    response = requests.post('http://127.0.0.1:8000/api-auth/points/')
    points = response.json()
    print(points)
    return render(request, 'home.html', {})
