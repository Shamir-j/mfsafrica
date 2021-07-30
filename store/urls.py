from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views
app_name = 'store'
from .views import (points_list, create_point)

urlpatterns = [
    path('pointslist/', views.points_list, name='home'),
    path('createpoint/', views.create_point),
]

