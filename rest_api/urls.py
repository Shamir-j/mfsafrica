from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PointAPIView, PointDetailAPIView

urlpatterns = [
    path('points/', PointAPIView.as_view()),
    path('pointdetail/<int:pk>/', PointDetailAPIView.as_view()),
]

